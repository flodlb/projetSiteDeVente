import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vetement',
            fields=[
                ('id_V', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('qnte', models.IntegerField(null=True)),
                ('prix', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='vetements/')),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id_P', models.AutoField(primary_key=True, serialize=False)),
                ('CommandeV', models.BooleanField(verbose_name=False)),
                ('qnte', models.IntegerField(null=True)),
                ('id_U', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_V', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.vetement')),
            ],
        ),
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('id_H', models.AutoField(primary_key=True, serialize=False)),
                ('id_Commande', models.IntegerField(null=True)),
                ('id_P', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.panier')),
            ],
        ),
    ]
