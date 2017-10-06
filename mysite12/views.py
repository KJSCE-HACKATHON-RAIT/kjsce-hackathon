from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world") 

def home_page(request):
	return HttpResponse("Home Page")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)

def current_datetime1(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
