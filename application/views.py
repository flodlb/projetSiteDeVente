
from django.shortcuts import render
from application.models import Vetement
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic


def liste_vetements(request):
    context = {}
    context["vetements"] = Vetement.objects.all()
    return render(request, 'application/affichage_des_vetements.html', context)

    
@login_required(login_url='compte:login')
def index(request):
    return render(request, "application/index.html")
    
@login_required(login_url='compte:login')
def home(request):
    return render(request,"application/home.html")
