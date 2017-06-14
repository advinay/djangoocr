from django.shortcuts import render, get_object_or_404

from django.template import RequestContext
from .models import *

from django.db.models import Q
from itertools import chain
from datetime import datetime
from django import template



def vue_profil(request, pk):

    user = get_object_or_404(User, pk=pk)
    # derniers_statuts=Statut.objects.filter(auteur=user).order_by('-date')[:3]
    liste_statuts=Statut.objects.filter(Q(auteur=user)).order_by('-date')
    liste_messages=Message.objects.filter(Q(destinataire=user)).order_by('-date')
    # result_list=Message.objects.filter(Q(auteur=user) | Q(destinataire=user))
    result_list=sorted(chain(liste_statuts,liste_messages),key=lambda instance: instance.date,reverse=True)
    date_actuelle=datetime.now()
    # result=result_list[0]
    # print (result.comment_set.all())

    return render(request, 'social/profil.html',{'user': user,'result_list':result_list,'date_actuelle':date_actuelle})

def accueil(request):

	return vue_profil(request,User.objects.first().pk)
