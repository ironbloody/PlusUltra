from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Publicacion, IdiomaPublicacion
from django.contrib.auth.models import User

###
class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "email")

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ("username", "email")

###
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ("titulo", "fecha", "revista", "investigador")
        
        #https://docs.djangoproject.com/en/4.0/ref/forms/widgets/
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': True}),
            'revista': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'investigador': forms.SelectMultiple(attrs={'class': 'form-control', 'required': True}),
        }
        
###
class IdiomaPublicacionForm(forms.ModelForm):
    # recibe el id de la publicación para agregarla al formulario.
    def __init__(self, *args, **kwargs):
        publicacion = kwargs.pop('publicacion')
        super(IdiomaPublicacionForm, self).__init__(*args, **kwargs)
        self.fields['publicacion'].initial = publicacion
        
    class Meta:
        model = IdiomaPublicacion
        fields = ("publicacion", "idioma", "fecha",)
        
        widgets = {
            'publicacion': forms.TextInput(attrs={'class': 'form-control', 'readonly': True, 'required': True}),
            'idioma': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': True}),
        }
        
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
        
