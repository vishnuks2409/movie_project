from django import forms
from .models import Movie

class Moviefrom(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'