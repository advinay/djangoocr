from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('pseudo',)
    # list_filter = ('categorie', )
    # search_fields = ('title', 'auteur', )

    # prepopulated_fields = {'slug': ('titre', )}


class StatutAdmin(admin.ModelAdmin):
	list_display = ('auteur','contenu','date')

class MessageAdmin(admin.ModelAdmin):
	list_display = ('auteur','contenu','date','destinataire')

class CommentAdmin(admin.ModelAdmin):
	list_display=('auteur_comment','statut_comment','text_comment','date')


admin.site.register(User, UserAdmin)
admin.site.register(Statut, StatutAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Comment,CommentAdmin)