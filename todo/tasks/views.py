from django.shortcuts import render
from django.http import HttpResponse

#create views
def index(request):
    return HttpResponse ('hello world')

