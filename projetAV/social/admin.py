from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('pseudo',)
    # list_filter = ('categorie', )
    # search_fields = ('title', 'auteur', )

    # prepopulated_fields = {'slug': ('titre', )}


class StatutAdmin(admin.ModelAdmin):
	list_display = ('auteur','contenu','date')


admin.site.register(User, UserAdmin)
admin.site.register(Statut, StatutAdmin)