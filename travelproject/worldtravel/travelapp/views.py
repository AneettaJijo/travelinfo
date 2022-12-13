from django.http import HttpResponse
from django.shortcuts import render
from . models import Picture
from . models import Team

# Create your views here.
def travelling(request):
    obj=Picture.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})