from django.shortcuts import render
from .models import Project
# Create your views here.

def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects_index.html', { 'projects': projects })