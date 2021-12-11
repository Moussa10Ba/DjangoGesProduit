# Generated by Django 3.2.4 on 2021-12-09 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('date_creation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=30)),
                ('quantite', models.IntegerField()),
                ('reference', models.CharField(max_length=30)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gesProduit.categorie')),
            ],
        ),
    ]