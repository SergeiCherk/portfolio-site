from django.shortcuts import render
from .models import AboutMe, Skill

def index(request):
    about = AboutMe.objects.first()
    skills = Skill.objects.all()
    context = {
        'about': about,
        'skills': skills,
    }
    return render(request, 'about/index.html', context)