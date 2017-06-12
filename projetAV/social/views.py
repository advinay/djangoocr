from django.shortcuts import render, get_object_or_404

from django.template import RequestContext
from .models import *

from django.views.generic import ListView,DetailView



def vue_profil(request, pk):

    user = get_object_or_404(User, pk=pk)
    derniers_statuts=Statut.objects.filter(auteur=user).order_by('-date')[:3]

    return render(request, 'social/profil.html',{'user': user,'derniers_statuts': derniers_statuts})

def accueil(request):

	return vue_profil(request,User.objects.latest('pk').pk)
