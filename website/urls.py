from django.urls import path
from .views import home, submit_form

urlpatterns = [
    path('', home),
    path("submit/", submit_form, name="submit_form"),
]
