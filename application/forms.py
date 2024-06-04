
from django import forms
from .models import Panier, Vetement


class AjouterAuPanierForm(forms.ModelForm):
    qnte = forms.IntegerField(
        label='Quantité souhaitée',
        min_value=1,
        error_messages={'min_value': 'La quantité doit être au moins 1.'}
    )

    class Meta:
        model = Panier
        fields = ['qnte']


class VetementForm(forms.ModelForm):
    class Meta:
        model = Vetement
        fields = ['nom', 'description', 'qnte', 'prix', 'image']
