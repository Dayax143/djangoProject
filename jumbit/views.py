from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
    #return HttpResponse("<h1 style='text-align:center; color:blue'>welcome python webApp</h1>")

def dashboard(request):
    return render(request, "dashboard.htm")