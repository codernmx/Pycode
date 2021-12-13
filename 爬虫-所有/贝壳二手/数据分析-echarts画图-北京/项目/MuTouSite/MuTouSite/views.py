from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def fang(request):
    return render(request, 'fang.html')

def lei(request):
    return render(request, 'lei.html')

def big(request):
    return render(request, 'big.html')
