from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("contact/", contact, name="contact"),
    
    path("subscribe/", subscribe, name="subscribe"),
    
]