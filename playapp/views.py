
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import Student
import uuid

def hello_world(request):
    return render(request, "hello.html")


# simply utility function
def calculate():
    return "This is calculate function"

# list of online vote options
RegisteredUsers = {}
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





# ---------------- STUDENT LOGIN PAGE ----------------
def student_login(request):
    message = ""

    if request.method == "POST":
        roll = request.POST.get("username")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(roll=roll)
            if student.password == password:
                return HttpResponse("<h1>Login Successful! Welcome Student.</h1>")
            else:
                message = "Incorrect Password"
        except Student.DoesNotExist:
            message = "Roll Number not registered"

    return render(request, "student_login.html", {"message": message})


# ---------------- STUDENT REGISTRATION PAGE ----------------
def student_register(request):
    message = ""

    if request.method == "POST":
        fullname = request.POST.get("fullname")
        roll = request.POST.get("roll")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        # AUTO-GENERATED EMAIL (student MUST NOT enter email)
        email = f"{roll}@uog.edu.pk"

        # VALIDATION
        if len(roll) != 12:
            message = "Roll number must be 12 characters."
        elif password != confirm:
            message = "Passwords do not match."
        elif Student.objects.filter(roll=roll).exists():
            message = "Roll Number already registered."
        else:
            Student.objects.create(
                fullname=fullname,
                roll=roll,
                email=email,     # auto email
                password=password
            )
            return redirect("/student/login/")

    return render(request, "student_register.html", {"message": message})


#--forget password--#
def forgot_password(request):
    message = ""

    if request.method == "POST":
        roll = request.POST.get("roll")

        # Generate email from roll number
        email = f"{roll}@uog.edu.pk"

        try:
            student = Student.objects.get(roll=roll)
        except Student.DoesNotExist:
            return render(request, "student/forget_password.html",
                {"message": "Roll number is not registered!"})

        # CREATE PASSWORD RESET TOKEN
        token = str(uuid.uuid4())
        reset_tokens[token] = student.roll

        reset_link = request.build_absolute_uri(
            reverse("reset-password") + f"?token={token}"
        )

        # SEND EMAIL
        send_mail(
            "Reset Your Password",
            f"Click the link to reset your password:\n{reset_link}",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        message = "Reset password link sent to your email!"

    return render(request, "student/forget_password.html", {"message": message})





     #reset [password#]
def reset_password(request):
    token = request.GET.get("token")

    if token not in reset_tokens:
        return render(request, "student/reset_password.html",
                      {"message": "Invalid or expired link!"})

    roll = reset_tokens[token]

    if request.method == "POST":
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            return render(request, "student/reset_password.html",
                          {"message": "Passwords do not match!"})

        student = Student.objects.get(roll=roll)
        student.password = password
        student.save()

        del reset_tokens[token]
        return redirect("/student/login/")

    return render(request, "student/reset_password.html")