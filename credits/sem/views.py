from django.shortcuts import render
from django.http import HttpResponse
from sem.models import *
# Create your views here.


def home(request):
    """help"""
    branches = Branch.objects.all()
    
    context = {"branches":branches}
    return render(request, 'index.html', context)


def sem(request,pk):
    branch = Branch.objects.get(id=pk)
    semesters = branch.semesters.all()
    return render(request, 'semester.html',{"semesters":semesters})


def sub(request,pk):
    subjects = Semester.objects.get(id=pk).subjects.all()
    return render(request,'subject.html',{"subjects":subjects})

def lecture(request):
    course = Course.objects.all()
    return render(request,'lecture.html')
