from django import forms
from django.forms.models import inlineformset_factory
from .models import Article, Investigator, Superhero, SuperheroImage

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


class SuperheroForm(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = ['name', 'identity', 'description', 'strength', 'weakness']

SuperheroImageFormSet = inlineformset_factory(
    Superhero,
    SuperheroImage,
    form=forms.ModelForm,
    fields=['image'],
    extra=0,
    can_delete=True
)
