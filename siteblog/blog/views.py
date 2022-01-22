from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, template_name='blog/index.html')

# Create your views here.
