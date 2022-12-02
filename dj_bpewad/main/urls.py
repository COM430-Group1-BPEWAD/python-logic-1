from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                    # Top two urls go to the same page, might be a bad idea to do it this way
    path("login", views.index, name="index"),
    path("signup", views.signup, name="signup"),            # Links to the Signup Page
    path("create/", views.createAccount, name="Logged In"),
    path("test2", views.surveyform, name="survey"),         # Test links to the Survey
    path('patient/information/', views.patientInfoView, name="Personal details"),
    path('patient/<int:id>/information', views.patientIdInfoView, name="Personal details"),
    path('patient/<int:id>/new-reading', views.newReading, name="New Blood Pressure Reading"),
    path('patient/<int:id>/report/', views.recordBP),
    path('patient/<int:id>/emt', views.emt),
    path('patient/<int:id>/emergency', views.emergency),
    path('patient/<int:id>/history', views.history),
    path('patient/<int:id>/panel', views.viewPanel, name="Patient Dash")
]