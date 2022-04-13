#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django import forms
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

from library.models import Book, Reader, User, Borrowing
from library.forms import SearchForm, LoginForm, RegisterForm, ResetPasswordForm


def index(request):
    context = {
        'searchForm': SearchForm(),
    }
    return render(request, 'library/index.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    state = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse(u'Your account is disabled.')
        else:
            state = 'not_exist_or_password_error'

    context = {
        'loginForm': LoginForm(),
        'state': state,
    }

    return render(request, 'library/login.html', context)


def user_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    registerForm = RegisterForm()

    state = None
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST, request.FILES)
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('re_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            name = request.POST.get('name', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create(username=username)
                new_user.set_password(password)
                new_user.save()
                new_reader = Reader.objects.create(user=new_user, name=name, phone=int(username))
                new_reader.photo = request.FILES['photo']
                new_reader.save()
                state = 'success'

                auth.login(request, new_user)

                context = {
                    'state': state,
                    'registerForm': registerForm,
                }
                return render(request, 'library/register.html', context)

    context = {
        'state': state,
        'registerForm': registerForm,
    }

    return render(request, 'library/register.html', context)


@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')

        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'

    context = {
        'state': state,
        'resetPasswordForm': ResetPasswordForm(),
    }

    return render(request, 'library/set_password.html', context)


@login_required
def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    id = request.user.id
    try:
        reader = Reader.objects.get(user_id=id)
    except Reader.DoesNotExist:
        return HttpResponse('no this id reader')

    borrowing = Borrowing.objects.filter(reader=reader).exclude(date_returned__isnull=False)

    context = {
        'state': request.GET.get('state', None),
        'reader': reader,
        'borrowing': borrowing,
    }
    return render(request, 'library/profile.html', context)


def reader_operation(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    action = request.GET.get('action', None)

    if action == 'return_book':
        id = request.GET.get('id', None)
        if not id:
            return HttpResponse('no id')
        b = Borrowing.objects.get(pk=id)
        b.date_returned = datetime.date.today()
        if b.date_returned > b.date_due_to_returned:
            b.amount_of_fine = (b.date_returned - b.date_due_to_returned).total_seconds() / 24 / 3600 * 0.1
        b.save()

        r = Reader.objects.get(user=request.user)
        r.max_borrowing += 1
        r.save()

        bk = Book.objects.get(ISBN=b.ISBN_id)
        bk.quantity += 1
        bk.save()

        return HttpResponseRedirect('/profile?state=return_success')

    elif action == 'renew_book':
        id = request.GET.get('id', None)
        if not id:
            return HttpResponse('no id')
        b = Borrowing.objects.get(pk=id)
        if (b.date_due_to_returned - b.date_issued) < datetime.timedelta(60):
            b.date_due_to_returned += datetime.timedelta(30)
            b.save()

        return HttpResponseRedirect('/profile?state=renew_success')

    return HttpResponseRedirect('/profile')


def book_search(request):
    search_by = request.GET.get('search_by', '书名')
    books = []
    current_path = request.get_full_path()

    keyword = request.GET.get('keyword', u'_书目列表')

    if keyword == u'_书目列表':
        books = Book.objects.all()
    else:
        if search_by == u'书名':
            keyword = request.GET.get('keyword', None)
            books = Book.objects.filter(title__contains=keyword).order_by('-title')[0:50]
        elif search_by == u'ISBN':
            keyword = request.GET.get('keyword', None)
            books = Book.objects.filter(ISBN__contains=keyword).order_by('-title')[0:50]
        elif search_by == u'作者':
            keyword = request.GET.get('keyword', None)
            books = Book.objects.filter(author__contains=keyword).order_by('-title')[0:50]

    paginator = Paginator(books, 5)
    page = request.GET.get('page', 1)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    # ugly solution for &page=2&page=3&page=4
    if '&page' in current_path:
        current_path = current_path.split('&page')[0]

    context = {
        'books': books,
        'search_by': search_by,
        'keyword': keyword,
        'current_path': current_path,
        'searchForm': SearchForm(),
    }
    return render(request, 'library/search.html', context)


def book_detail(request):
    ISBN = request.GET.get('ISBN', None)
    print(ISBN)
    if not ISBN:
        return HttpResponse('there is no such an ISBN')
    try:
        book = Book.objects.get(pk=ISBN)
    except Book.DoesNotExist:
        return HttpResponse('there is no such an ISBN')

    action = request.GET.get('action', None)
    state = None

    if action == 'borrow':

        if not request.user.is_authenticated:
            state = 'no_user'
        else:
            reader = Reader.objects.get(user_id=request.user.id)
            if reader.max_borrowing > 0:
                reader.max_borrowing -= 1
                reader.save()

                bk = Book.objects.get(pk=ISBN)
                bk.quantity -= 1
                bk.save()

                issued = datetime.date.today()
                due_to_returned = issued + datetime.timedelta(30)

                b = Borrowing.objects.create(
                    reader=reader,
                    ISBN=bk,
                    date_issued=issued,
                    date_due_to_returned=due_to_returned)

                b.save()
                state = 'success'
                return HttpResponseRedirect('/profile?state=borrow_success')
            else:
                state = 'upper_limit'

    context = {
        'state': state,
        'book': book,
    }
    return render(request, 'library/book_detail.html', context)


def statistics(request):
    borrowing = Borrowing.objects.all()
    readerInfo = {}
    for r in borrowing:
        if r.reader.name not in readerInfo:
            readerInfo[r.reader.name] = 1
        else:
            readerInfo[r.reader.name] += 1

    bookInfo = {}
    for r in borrowing:
        if r.ISBN.title not in bookInfo:
            bookInfo[r.ISBN.title] = 1
        else:
            bookInfo[r.ISBN.title] += 1

    readerData = list(sorted(readerInfo, key=readerInfo.__getitem__, reverse=True))[0:10]
    bookData = list(sorted(bookInfo, key=bookInfo.__getitem__, reverse=True))[0:5]

    readerAmountData = [readerInfo[x] for x in readerData]

    bookAmountData = [bookInfo[x] for x in bookData]

    context = {
        'readerData': readerData,
        'readerAmountData': readerAmountData,
        'bookData': bookData,
        'bookAmountData': bookAmountData,
    }
    return render(request, 'library/statistics.html', context)


def about(request):
    return render(request, 'library/about.html', {})
