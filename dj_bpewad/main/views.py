from django.shortcuts import render
from django.http import HttpResponse
from .forms import login, signupform

# Create your views here.

# Goes to the login page. Creates form from forms.py
def index(response):
    #return HttpResponse('<h1>hello world</h1>')
    form = login()
    return render(response, "main/login.html", {"form": form})

# Goes to the signup page. Creates form from forms.py
def signup(response):
    form = signupform()
    return render(response, "main/signup.html", {"form": form})

# Goes to the User Panel. Currently static HTML
def viewPanel(response):
    return render(response, "main/panel.html")

#Goes to the Survey. Currently static HTML
def surveyform(response):
    return render(response, "main/survey.html")