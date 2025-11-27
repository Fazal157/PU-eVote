from django.shortcuts import render
from django.hhtp import HttpResponse

# Create your views here.
# request -> response
# request handler
# action
def say_hello(request):
    return render(request, 'hello.html')
#pull data from db
#Transform
#send email
