
from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return render(request, "hello.html")


# simply utility function
def calculate():
    return "This is calculate function"

# list of online vote options
VotePanel = [
    {
        "id": 1,
        "name": "Student",
        "image": "https://news.uchicago.edu/sites/default/files/styles/gallery/public/images/2019-07/Mobile%20voting.jpg?h=944f5cba&itok=nO2RUYXv"
    },
    {
        "id": 2,
        "name": "Coordinator",
        "image": "https://stateline.org/wp-content/uploads/2019/07/16x9_M-3.jpg"
    },
    {
        "id":3,
        "name":"Admin",
        "image":"https://adminlte.io/uploads/images/blog/05/027-Gentelella-Alela-colorlib.com_.png"
    }
]
def home(request):
    return render(request, "hello.html", {"VotePanel": VotePanel})