from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def Home_page_view(request):
    return HttpResponse('<h1>this is the first web page</h1>')
def about_view(requst):
    return HttpResponse('<h1>about of site i creat this</h1>')
def contact_view(request):
    return HttpResponse('<h1> hi this is contact </h1>')
    