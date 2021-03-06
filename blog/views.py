from django.shortcuts import render, get_object_or_404

from .models import Article, Categorie, Comment
from .forms import CommentateurForm

from django.template import RequestContext
from django.views.generic import ListView,DetailView

# def accueil(request):
#     """
#     Affiche les 5 derniers articles du blog. Nous n'avons pas encore
#     vu comment faire de la pagination, donc on ne donne pas la
#     possibilité de lire les articles plus vieux via l'accueil pour
#     le moment.
#     """
#     articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

#     return render(request, 'blog/accueil.html', {'articles': articles})


# def lire_article(request, slug):
#     """
#     Affiche un article complet, sélectionné en fonction du slug
#     fourni en paramètre
#     """
#     article = get_object_or_404(Article, slug=slug)

#     lastcomments=Comment.objects.filter(article=article,is_visible=True).order_by('-date')[:3]

#     #lastcomment=queryset[0]
#     envoi=False

#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = CommentateurForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#         #     # process the data in form.cleaned_data as required
#             pseudo=form.cleaned_data['pseudo']
#             commentateur_email=form.cleaned_data['commentateur_email']
#             contenu_commentaire=form.cleaned_data['contenu_commentaire']
#             c=Comment(article=article,pseudo=pseudo,email=commentateur_email,is_visible=True,contenu=contenu_commentaire)
#             c.save()
#             envoi=True 
#         #     # redirect to a new URL:
#         #     return HttpResponseRedirect(slug)

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = CommentateurForm()

#     return render(request, 'blog/lire_article.html',{'article': article,'lastcomments':lastcomments,'form':form,'envoi':envoi})


class ListeArticles(ListView):
    model = Article
    context_object_name = "derniers_articles"
    template_name = "blog/accueil.html"
    paginate_by = 5


    def get_context_data(self, **kwargs):
    # Nous récupérons le contexte depuis la super-classe
        context = super(ListeArticles, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context

class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire_article.html"

def test(request):

    taux_change = 3.1415
    return render(request,'blog/test.html', {'taux': taux_change})

