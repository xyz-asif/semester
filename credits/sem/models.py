from django.db import models

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=200, null=True,unique=True,blank=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=200, null=True,unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200, null=True,unique=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200, null=True,unique=True)
    Quest = models.FileField(upload_to='quest')
    Pdf = models.FileField(upload_to='pdfs')
    Video = models.FileField(upload_to='videos')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
