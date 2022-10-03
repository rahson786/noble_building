from django.shortcuts import render

from noble_building_llc.models import People, Project

# Create your views here.
def home(request):
    return render(request, 'noble_building_llc/home.html')


def about(request):
    people = People.objects.all()
    return render(request, 'noble_building_llc/about.html', {'peoples' : people})


def contact(request):
    return render(request, 'noble_building_llc/contact.html')


def projects(request):
    project = Project.objects.all()
    return render(request, 'noble_building_llc/projects.html', {'projects' : project})


def services(request):
    return render(request, 'noble_building_llc/services.html')