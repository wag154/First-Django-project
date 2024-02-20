from django.shortcuts import render,HttpResponse
from .models import First_Model
# Create your views here.
def home (request):
    return HttpResponse("Hello world")

def Return_todo (request) :
    items = First_Model.objects.all()
    return HttpResponse ("Todo returned")