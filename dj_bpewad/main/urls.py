from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                    # Top two urls go to the same page, might be a bad idea to do it this way
    path("login", views.index, name="index"),
    path("signup", views.signup, name="signup"),            # Links to the Signup Page
    path("test", views.viewPanel),                          # Test links to the User Panel
    path("test2", views.surveyform, name="survey"),         # Test links to the Survey
]