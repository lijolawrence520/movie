from django import forms
from.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.TextInput(attrs={'class': 'form-control'}),
                   'year': forms.DateInput(attrs={'class': 'form-control'}),
                   'img': forms.FileInput(attrs={'class': 'form-control'}),
                   }
