from django.shortcuts import render
from django.http import HttpResponse
from sem.models import *
# Create your views here.


def home(request):
    """help"""
    branch = Branch.objects.all()
    
    context = {"branch":branch}
    return render(request, 'index.html', context)


def sem(request,pk):
    semester = Semester.objects.get(id=pk)
    return render(request, 'semester.html',{"semester":semester})


def sub(request):
    subject = Subject.objects.all()
    return render(request,'subject.html',{"subject":subject})

def lecture(request):
    course = Course.objects.all()
    return render(request,'lecture.html')
