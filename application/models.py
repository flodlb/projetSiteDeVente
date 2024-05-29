from django.db import models
from django.contrib.auth.models import User


class Vetement(models.Model):
    nom = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    qnte = models.IntegerField(null=True)
    prix = models.IntegerField(null=True)

    def __str__(self):
        return self.nom



class Panier(models.Model):
    id_P = models.AutoField(primary_key=True)
    CommandeV = models.BooleanField(False)
    id_V = models.ForeignKey(Vetement, on_delete=models.CASCADE)
    id_U = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Panier {self.id} - Commande validée: {self.CommandeV}"


class Historique(models.Model):
    id_H = models.AutoField(primary_key=True)
    id_Commande = models.IntegerField(null=True)
    id_P = models.ForeignKey(Panier, on_delete=models.CASCADE)
    def __str__(self):
        return f'Historique for Commande {self.id_Commande} and Panier {self.id_P.id}'
