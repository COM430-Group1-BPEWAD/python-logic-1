from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .forms import login, signupform
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import patient
from django.shortcuts import get_object_or_404

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

@csrf_exempt
def createAccount(response):
    answers = response.POST
    print(answers)
    newPatient = patient.objects.create(
        patientUserName=response.POST['uName'],
        firstName=response.POST['fName'],
        lastName=response.POST['lName'],
        email=response.POST['email'],
        phone=response.POST['phone'],
        address=response.POST['address'],
        allergies=response.POST['allergies']
    )
    newPatient.save()
    return render(response, "main/panel.html")

def patientInfoView(request, patient_id):
    patientInfo = get_object_or_404(patient, pk=patient_id)
    print(patientInfo)
    return render(request, "main/patient-info.html", {'patient': patientInfo})

#Goes to the Survey. Currently static HTML
def surveyform(response):
    return render(response, "main/survey.html")