from django import forms
from .models import Autor, Livros
from django.contrib.auth.forms import UserCreationForm

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'cpf', 'data_nascimento']

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livros
        fields = "__all__"
class MyUserCreationForm(UserCreationForm):
    pass