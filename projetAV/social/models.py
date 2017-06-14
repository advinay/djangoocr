from django.db import models

class User(models.Model):
    pseudo = models.CharField(max_length=20)

    def __str__(self):
        return self.pseudo


class Statut(models.Model):

    auteur=models.ForeignKey(User, related_name='auteur')
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date message",
                                auto_now_add=False, auto_now=True)

    def __str__(self):

        return (self.auteur.pseudo+":"+self.contenu)

class Message(Statut):
        destinataire=models.ForeignKey(User, related_name='destinataire_message')

class Comment(models.Model):
    auteur_comment=models.ForeignKey(User,related_name="auteur_comment")
    statut_comment=models.ForeignKey('Statut')
    text_comment=models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date_commentaire",
                                auto_now_add=False, auto_now=True)
