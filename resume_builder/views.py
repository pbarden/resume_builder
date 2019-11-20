from django.shortcuts import render
from .models import UserProfile, Job, Skill, Degree, Project

# Create your views here.
def home(request):
    profiles = UserProfile.objects.all()
    jobs = Job.objects.all()
    skills = Skill.objects.all()
    degrees = Degree.objects.all()
    projects = Project.objects.all()
    return render(request, 'base.html', {'profiles': profiles, 'jobs': jobs, 'skills': skills, 'degrees': degrees, 'projects': projects})