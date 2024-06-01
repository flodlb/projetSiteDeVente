from django.db.models.functions import datetime
from django.shortcuts import render, get_object_or_404, redirect

from application.forms import AjouterAuPanierForm
from application.models import Vetement, Panier, Historique
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic


def viewVetements(request):
    context = {}
    context["vetements"] = Vetement.objects.all()
    return render(request, 'application/viewVetement.html', context)


def viewZoom(request, pk):
    vetement = get_object_or_404(Vetement, id_V=pk)
    form = AjouterAuPanierForm()
    context = {
        'vetement': vetement,
        'form': form
    }
    return render(request, 'application/viewZoom.html', context)


def addToPanier(request, pk):
    vetement = get_object_or_404(Vetement, id_V=pk)
    if request.method == 'POST':
        print(request.method)
        form = AjouterAuPanierForm(request.POST or None)

        if form.is_valid():
            qnte = form.cleaned_data['qnte']
            if vetement.qnte >= qnte:
                # Update the stock of the vetement
                vetement.qnte -= qnte
                vetement.save()

            # Create or update the panier item
            panier_item, created = Panier.objects.get_or_create(
                id_U=request.user,
                id_V=vetement,
                CommandeV=False,
                defaults={'qnte': qnte}
            )
            if not created:
                panier_item.qnte += qnte
                panier_item.save()
            return redirect('application:viewPanier')
        else:
            error_message = "Quantité demandée non disponible"
            return render(request, 'application/viewZoom.html', {
                'vetement': vetement,
                'form': form,
                'error_message': error_message
            })
    else:
        form = AjouterAuPanierForm()

    return render(request, 'application/viewZoom.html', {
        'vetement': vetement,
        'form': form
    })


def ValidePanier(request):
    if request.method == 'POST':
        panier_items = Panier.objects.filter(id_U=request.user, CommandeV=False)
        if panier_items.exists():
            id_commande = int(datetime.datetime.now().timestamp())
            for item in panier_items:
                item.CommandeV = True
                item.save()
                Historique.objects.create(id_Commande=id_commande, id_P=item)
        return redirect('application:viewPanier')
    return render(request, 'application/viewPanier.html')


def viewHistorique(request):
    historiques = Historique.objects.filter(id_P__id_U=request.user)
    return render(request, 'application/viewHistorique.html', {'historiques': historiques})



def viewPanier(request):
    panier_items = Panier.objects.filter(id_U=request.user, CommandeV=False)
    return render(request, 'application/viewPanier.html', {'panier_items': panier_items})


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'home'
    template_name = "application/index.html"


@login_required(login_url='home')
def list_view(request):
    return render(request, 'application/home.html')


@login_required(login_url='compte:login')
def home(request):
    return render(request, "application/home.html")
