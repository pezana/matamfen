from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(etudiant)
admin.site.register(inscription)
admin.site.register(formation)
admin.site.register(anneeacademique)
admin.site.register(profmatiere)
admin.site.register(notes)
class listeetudiant(ImportExportModelAdmin):
    liste_display=('nom','prenom')


