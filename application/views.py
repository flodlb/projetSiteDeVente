from django.shortcuts import render
from application.models import Vetement


def liste_vetements(request):
    context = {}
    context["vetements"] = Vetement.objects.all()
    return render(request, 'application/affichage_des_vetements.html', context)