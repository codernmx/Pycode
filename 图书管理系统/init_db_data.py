#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slack_management.settings')

import django

django.setup()

import json
import argparse
import random
import datetime
import codecs
import os.path as op
from library.models import Book, Reader, Borrowing
from django.contrib.auth.models import User

from faker import Factory

fake = Factory.create('zh_CN')


def init_reader_data(amount=50):
    for i in range(amount):
        u = User.objects.get_or_create(username=fake.phone_number())[0]
        u.set_password('password')
        u.save()

        r = Reader.objects.get_or_create(user=u, name=fake.name(), phone=int(u.username))[0]
        r.balance = round(random.random() * 100, 2)
        r.photo = str(r.user_id) + '.jpg'
        r.save()


def init_book_data():
    with codecs.open('books.json', 'r', 'utf-8') as f:
        books = json.load(f)

    for b in books:
        if 'content_description' in b and b['content_description']:
            print(b)
            try:
                B = Book.objects.get_or_create(ISBN=b['ISBN'], title=b['name'], author=b['author'], press=b['press'])[0]
                B.description = b['content_description']
                B.price = b['price']
                B.cover = b['cover']
                B.quantity = random.randint(0, 7)
                B.save()
            except KeyError:
                continue


def init_borrowing_data(amount=50):
    for i in range(amount):
        reader = random.choice(Reader.objects.all())
        isbn = random.choice(Book.objects.all())
        issued = datetime.date.today() + datetime.timedelta(random.randint(1, 30))
        due_to_returned = issued + datetime.timedelta(30)
        date_returned = issued + datetime.timedelta(random.randint(1, 40))
        returned_flag = True

        if random.randint(1, 100) % 2 == 0:
            returned_flag = False

        if returned_flag:
            if (date_returned - issued).days > 30:
                fine = ((date_returned - issued).days - 30) * 0.1
            else:
                fine = 0

            b = Borrowing.objects.create(
                reader=reader,
                ISBN=isbn,
                date_issued=issued,
                date_due_to_returned=due_to_returned,
                date_returned=date_returned,
                amount_of_fine=fine,
            )
            b.save()
        else:

            if reader.max_borrowing > 0 and isbn.quantity > 0:
                b = Borrowing.objects.create(
                    reader=reader,
                    ISBN=isbn,
                    date_issued=issued,
                    date_due_to_returned=due_to_returned
                )

                reader.max_borrowing -= 1
                isbn.quantity -= 1
                reader.save()
                isbn.save()
                b.save()


if __name__ == '__main__':
    init_book_data()

    parser = argparse.ArgumentParser()
    parser.add_argument("data", help=u"你要生成的数据")
    args = parser.parse_args()

    if args.data == 'all':
        init_reader_data()
        init_book_data()
        init_borrowing_data()
    elif args.data == 'book':
        init_book_data()
    elif args.data == 'reader':
        init_reader_data()
    elif args.data == 'borrowing':
        init_borrowing_data()
