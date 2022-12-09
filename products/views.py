from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def index(request):
    items = Products.objects.all()
    return render(request, 'index.html', {'products': items})


def product(request):
    return HttpResponse('New products')
