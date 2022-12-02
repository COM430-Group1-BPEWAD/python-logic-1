from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .forms import login, signupform, bloodPressureForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import patient, bpReadings
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.

# Goes to the login page. Creates form from forms.py
def index(response):
    #return HttpResponse('<h1>hello world</h1>')
    form = login()
    return render(response, "templates/registration/login.html", {"form": form})

# Goes to the signup page. Creates form from forms.py
def signup(response):
    form = signupform()
    return render(response, "main/signup.html", {"form": form})

# Goes to the User Panel. Currently static HTML
def viewPanel(response, id):
    patientInfo = get_object_or_404(patient, id=id)
    return render(response, "main/panel.html", {'patient': patientInfo})

#@csrf_exempt
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
    )
    newPatient.save()
    return render(response, "home.html")

def patientInfoView(request):
    print(request.POST)
    patientInfo = get_object_or_404(patient, patientUserName=request.POST['uName'])
    print(patientInfo)
    return render(request, "main/patient-info.html", {'patient': patientInfo})

def patientIdInfoView(request, id):
    patientInfo = get_object_or_404(patient, id = id)
    return render(request, "main/patient-info.html", {'patient': patientInfo})

def newReading(request, id):
    patientInfo = get_object_or_404(patient, id=id)
    form = bloodPressureForm()
    return render(request, "main/new-reading.html", {"patient": patientInfo, "form": form})

def recordBP(request, id):
    patientInfo = get_object_or_404(patient, id=id)
    print(patientInfo)
    newBRReading = bpReadings.objects.create(
        patient_id = patientInfo,
        systolic = request.POST['systolic'],
        diastolic = request.POST['diastolic']
    )
    newBRReading.save()
    return render(request, "main/readingReceived.html", {'systolic': int(newBRReading.systolic), 'diastolic': int(newBRReading.diastolic), 'patient': patientInfo})

def emt(request, id):
    patientInfo = get_object_or_404(patient, id=id)
    return render(request, "main/emt.html", {'patient': patientInfo})

def emergency(request, id):
    patientInfo = get_object_or_404(patient, id=id)
    return render(request, "main/emergency.html", {'patient': patientInfo})

def history(request, id):
    patientInfo = get_object_or_404(patient, id=id)
    bp = get_list_or_404(bpReadings, patient_id=patientInfo)
    return render(request, "main/history.html", {'patient': patientInfo, 'bpReadings': bp})

#Goes to the Survey. Currently static HTML
def surveyform(response):
    return render(response, "main/survey.html")