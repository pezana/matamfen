# Generated by Django 4.0.4 on 2022-05-07 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anneeacademique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('an_libelle', models.CharField(help_text='entrer le libelle de l année académique', max_length=10)),
                ('an_ancienid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etud_nom', models.CharField(help_text='entrer le nom', max_length=50)),
                ('etud_prenom', models.CharField(help_text='entrer le prenom', max_length=50)),
                ('etud_date', models.DateField(blank=True, null=True)),
                ('etud_lieu', models.CharField(help_text='entrer le lieu de naissance', max_length=50)),
                ('etud_ancienid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='formasem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsem_semestre', models.CharField(help_text='entrer le semestre', max_length=50)),
                ('fsem_cycle', models.CharField(help_text='entrer le cycle', max_length=50)),
                ('fsem_niveau', models.CharField(help_text='entrer le niveau de la formation ', max_length=50)),
                ('fsem_ancienid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='formasue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsue_ue', models.CharField(max_length=50)),
                ('fsue_codeue', models.CharField(max_length=15)),
                ('fsue_creditue', models.IntegerField()),
                ('fsue_moduleue', models.CharField(max_length=50)),
                ('fsue_ancienid', models.IntegerField()),
                ('formasem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.formasem', verbose_name='formasem')),
            ],
        ),
        migrations.CreateModel(
            name='formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_libelle', models.CharField(help_text='Enter la formation', max_length=50)),
                ('for_tutelle', models.CharField(help_text='Enter la tutelle', max_length=50)),
                ('for_parcours', models.CharField(help_text='Enter le parcours', max_length=50)),
                ('for_ancien_idfor', models.IntegerField()),
                ('for_campus', models.CharField(help_text='entrer la campus', max_length=40)),
                ('for_domain', models.CharField(help_text='entrer le domaine', max_length=50)),
                ('for_filiere', models.CharField(help_text='entrer la filiere', max_length=50)),
                ('for_detailformation', models.CharField(help_text='entrer le detail de la formation', max_length=50)),
                ('for_periode', models.CharField(help_text='entrer la periode', max_length=50)),
                ('for_ancien_idetail', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_ancienid', models.IntegerField()),
                ('anneeacademique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.anneeacademique', verbose_name='anneeacademique')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.etudiant', verbose_name='etudiant')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.formation', verbose_name='formation')),
            ],
        ),
        migrations.CreateModel(
            name='profmatiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm_matiere', models.CharField(max_length=50)),
                ('pm_enseignant', models.CharField(max_length=50)),
                ('pm_creditpm', models.IntegerField()),
                ('pm_codepm', models.CharField(max_length=15)),
                ('pm_ancienid', models.IntegerField()),
                ('formasue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.formasue')),
            ],
        ),
        migrations.CreateModel(
            name='notesemestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ns_ancienid', models.IntegerField()),
                ('ns_moyenne', models.DecimalField(decimal_places=2, max_digits=2)),
                ('ns_creditsem', models.IntegerField()),
                ('ns_decision', models.CharField(max_length=10)),
                ('ns_session', models.CharField(max_length=15)),
                ('formasem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.formasem', verbose_name='formasem')),
                ('inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.inscription', verbose_name='inscription')),
            ],
        ),
        migrations.AddField(
            model_name='formasem',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.formation', verbose_name='formation'),
        ),
        migrations.CreateModel(
            name='emplois_de_temps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('em_jour', models.CharField(max_length=10)),
                ('em_ancienid', models.IntegerField()),
                ('em_hd', models.TimeField(blank=True, null=True)),
                ('em_hf', models.TimeField(blank=True, null=True)),
                ('anneeacademique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.anneeacademique', verbose_name='anneeacademique')),
                ('profmatiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moncompte.profmatiere', verbose_name='profmatiere')),
            ],
        ),
    ]