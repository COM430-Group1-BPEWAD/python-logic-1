from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls for login logic
    path("accounts/", include("django.contrib.auth.urls")),     # Links to the account registration app
    path("signup", views.signup, name="signup"),            # Links to the Signup Page
    path("create/", views.createAccount, name="Logged In"),
    path("registration_survey", views.surveyform, name="survey"),             # Test links to the Survey
    
    # urls for main dashboard and navigation
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("test", views.viewPanel), # Test links to the User Panel

    # path("", views.index, name="index"),                    # Top two urls go to the same page, might be a bad idea to do it this way
    # path("login", views.index, name="index"),
    
    
    # urls for database schema
    path('patient/information/', views.patientInfoView, name="Personal details"),
    path('patient/<int:id>/information', views.patientIdInfoView, name="Personal details"),
    path('patient/<int:id>/new-reading', views.newReading, name="New Blood Pressure Reading"),
    path('patient/<int:id>/report/', views.recordBP),
    path('patient/<int:id>/emt', views.emt),
    path('patient/<int:id>/emergency', views.emergency),
    path('patient/<int:id>/history', views.history),
    path('patient/<int:id>/panel', views.viewPanel, name="Patient Dash")
]