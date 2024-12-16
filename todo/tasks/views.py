from django.shortcuts import render
from django.http import HttpResponse

#create views
def index(request):
    return render(request,'tasks/list.html')


