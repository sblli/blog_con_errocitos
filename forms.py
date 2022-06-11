from django import forms
from .models import Contacto, publicacionn, otrapubli, comentario, Registro, login, uwu, postis
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#class="form-control" rows="5" id="publica"></textarea>
class postisform(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows':'5',
        'placeholder':'Tienes el poder de ayudar al cambio...'
    }))
    class Meta:
        model = postis
        fields = ('content','author',)

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class Publiform(forms.ModelForm):
    class Meta:
        model = publicacionn
        fields = '__all__'

class Otraform(forms.ModelForm):
    class Meta:
        model = otrapubli
        fields = '__all__'

class comentarioform(forms.ModelForm):
    class Meta:
        model = comentario
        fields = '__all__'

class RegisForm(forms.ModelForm):

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Registro.objects.filter(nombre=nombre).exists()

        if existe:
            raise ValidationError("Este nombre de usuario ya existe")

        return nombre

    class Meta:
        model = Registro
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass

class uwuform(forms.ModelForm):
    class Meta:
        model = uwu
        fields = '__all__'