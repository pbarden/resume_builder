from django.shortcuts import render
from .models import Job, Skill, Degree

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    skills = Skill.objects.all()
    degrees = Degree.objects.all()
    return render(request, 'base.html', {'jobs': jobs, 'skills': skills, 'degrees': degrees})