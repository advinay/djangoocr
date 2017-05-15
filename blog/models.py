from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",
                                     default=False)
    categorie = models.ForeignKey('Categorie')

    def __str__(self):
        return self.titre

    def nb_comment(self):
        a=self.comment_set.count()
        return a

    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.

    # def get_comments(self):
    #   comments=Comment.objects.get(article=self,is_visible=True)


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    """ Modèle pour les commentaires. A vous de l'écrire ! """
    article=models.ForeignKey('Article')
    pseudo = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    is_visible = models.BooleanField(verbose_name="Commentaire visible ?",
                                     default=True)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de commentaire",
                                auto_now_add=False, auto_now=True)

    def __str__(self):

        return self.pseudo


