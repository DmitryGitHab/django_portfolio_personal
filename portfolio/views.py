from django.shortcuts import render
from .models import Project, Stack
# Create your views here.

def home(request):
    projects = Project.objects.order_by('-date').all
    stacks = Stack.objects.order_by('-date').all
    return render(request, 'portfolio/home.html', {'projects': projects, 'stacks': stacks})

