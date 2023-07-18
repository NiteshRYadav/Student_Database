from django.shortcuts import render
from .models import Studentdata

# Create your views here.



def home(request):
    return render(request,'studentdetails/batch.html')

def index(request):
    data=Studentdata.objects.all()
    return render(request,'studentdetails/index.html',{"data":data})




def details(request,s):
    d=Studentdata.objects.get(slug=s)
    return render(request,'studentdetails/details.html',{"std_details":d})
