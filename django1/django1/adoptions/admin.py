from django.contrib import admin

from .models import Pet

@admin.register(Pet)
class PetAdmin( admin.ModelAdmin ):
    # address problem where listing is Pet Object
    # list the below columns in ajango admin
    list_display = [
        'name',
        'species',
        'breed',
        'age',
        'sex'
    ]