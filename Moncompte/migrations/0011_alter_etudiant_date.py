# Generated by Django 4.0.4 on 2022-05-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moncompte', '0010_alter_inscription_ancienid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]