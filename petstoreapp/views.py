from django.shortcuts import render

# Create your views here.
from .models import Pet

# Create your views here.


def allpets(req):
    petsdata = Pet.objects.all()
    context = {"petsdata": petsdata}
    return render(req, "allpets.html", context)


def displaypets(req, id):
    petsdata = Pet.objects.get(id=id)
    context = {"petsdata": petsdata}
    return render(req, "displaypets.html", context)
