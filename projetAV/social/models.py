from django.db import models

class User(models.Model):
    pseudo = models.CharField(max_length=20)

    def __str__(self):
        return self.pseudo


class Statut(models.Model):

    auteur=models.ForeignKey('User')
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date message",
                                auto_now_add=False, auto_now=True)

    def __str__(self):

        return self.auteur.pseudo

class Message(Statut):

	destinataire=models.ForeignKey('User')

	# def __str__(self):

 #    	return self.auteur

class Comment(models.Model):
	message=models.ForeignKey('Message')
	text_comment=models.TextField(null=True)
	date = models.DateTimeField(verbose_name="Date commentaire",
                                auto_now_add=False, auto_now=True)











    

