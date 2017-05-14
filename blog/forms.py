from django import forms

class CommentateurForm(forms.Form):
    pseudo = forms.CharField(label='pseudo', max_length=100,required=True)
    commentateur_email=forms.EmailField(label='email',max_length=254,required=True)
    contenu_commentaire=forms.CharField(widget=forms.Textarea)
