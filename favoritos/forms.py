from django import forms
from .models import Favorito

class FavoritoForm(forms.Form):
    nombre = forms.CharField()
    url = forms.URLField()

class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model = Favorito
        fields = '__all__'