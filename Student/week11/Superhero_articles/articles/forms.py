from django import forms
from .models import Article, Investigator

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


class InvestigatorForm(forms.ModelForm):
    class Meta:
        model = Investigator
        fields = ['name', 'biography']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your investigator name',
                'maxlength': '255',
            }),
            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a brief biography about yourself...',
                'rows': 5,
            }),
        }
        labels = {
            'name': 'Investigator Name',
            'biography': 'Your Biography',
        }