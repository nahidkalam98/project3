from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def string_response(request):
    return HttpResponse('This is my first string response')

def second_string(request):
    return HttpResponse('this is my second string response')

def third_string(request):
    return HttpResponse('This is my third string response')
