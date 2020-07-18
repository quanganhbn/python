from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Home view</h1>')

def pet_detail(request, pet_id):
    return HttpResponse(f'<p>detail view with id {pet_id}</p>')