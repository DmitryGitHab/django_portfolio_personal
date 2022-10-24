from django.shortcuts import render
from .models import Project, Stack, Сertificate


# Create your views here.

def home(request):
    projects = Project.objects.order_by('-date').all
    stacks = Stack.objects.order_by('-date').all
    certificates = Сertificate.objects.order_by('index').all()
    return render(request, 'portfolio/home.html', {'projects': projects,
                                                   'stacks': stacks,
                                                   'certificates': certificates,
                                                   })

