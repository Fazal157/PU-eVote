from django.shortcuts import render
from django.hhtp import HttpResponse

# Create your views here.
# request -> response
# request handler
# action
def hello_hello(request):
    return HttpResponse("Hello World")
#pull data from db
#Transform
#send email
