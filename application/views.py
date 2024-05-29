
from django.shortcuts import render
from application.models import Vetement, Panier
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic


def viewVetements(request):
    context = {}
    context["vetements"] = Vetement.objects.all()
    return render(request, 'application/viewVetement.html', context)
def viewPanier(request):
    context = {}
    context["panier"] = Panier.objects.all()
    return render(request, 'application/viewPanier.html', context)
#def viewZoom():
#   g = 5


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'home'
    template_name = "application/index.html"
    
@login_required(login_url='home')
def list_view(request):
    return render(request, 'application/home.html')
    
@login_required(login_url='compte:login')
def home(request):
    return render(request,"application/home.html")
