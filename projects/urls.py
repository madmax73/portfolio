from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "projects"

urlpatterns = [
    path("", projects_index, name="projects_index"),
    
] 