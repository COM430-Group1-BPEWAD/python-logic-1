from django import forms

# Form for username and password. On the home page
class login(forms.Form):
    uName = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=30)

# Form for entering initial patient information. Intended for signup.html
class signupform(forms.Form):
    uName = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())    # modified for security
    email = forms.EmailField(label="Email Address")
    phone = forms.CharField(label="Phone number", min_length=10, max_length=10)
    fName = forms.CharField(label="First Name", max_length=30)
    lName = forms.CharField(label="Last Name", max_length=30)
    address = forms.CharField(label="Address", max_length=60)

class surveyform(forms.Form):
    allergies = forms.CharField(label="Allergies", max_length=60)

class bloodPressureForm(forms.Form):
    systolic = forms.IntegerField(label = "Systolic reading (upper number)")
    diastolic = forms.IntegerField(label = "Diastolic reading (lower number)")