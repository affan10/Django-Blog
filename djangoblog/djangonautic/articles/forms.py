from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model  = models.Article
        fields = ['title', 'body', 'slug', 'thumb']

        # widgets = {
        #     'body': forms.Textarea(attrs={'rows': 15, 'cols': 90}),
        # }