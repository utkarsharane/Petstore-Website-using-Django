from django.contrib import admin

# Register your models here.
from .models import Pet

# Register your models here.


class PetAdmin(admin.ModelAdmin):
    list_display = [
        "petimage",
        "name",
        "species",
        "gender",
        "breed",
        "age",
        "description",
    ]


admin.site.register(Pet, PetAdmin)
