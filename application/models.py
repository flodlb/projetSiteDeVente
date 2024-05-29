from django.db import models
from django.contrib.auth.models import User

class Vetement(models.Model):
    vetement_description = models.CharField(max_length=200)
    qnte = models.IntegerField(null=True)
    prix = models.IntegerField(null=True)
    id_V = models.AutoField(primary_key=True)

    def __str__(self):
        return self.vetement_description

class Panier(models.Model):
    id_P = models.AutoField(primary_key=True)
    id_Commande = models.IntegerField(null=True)
    id_V = models.ForeignKey(Vetement, on_delete=models.CASCADE)
    id_U = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Panier {self.id_P} - Commande {self.id_Commande}"
