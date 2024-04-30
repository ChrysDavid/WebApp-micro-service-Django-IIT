# Generated by Django 5.0.4 on 2024-04-15 05:00

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='categorie_images')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id_produit', models.AutoField(primary_key=True, serialize=False)),
                ('nom_produit', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite_stock', models.IntegerField()),
                ('administrateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='listproduit.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='ImageProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='produit_images')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listproduit.produit')),
            ],
        ),
    ]