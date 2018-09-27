from django import forms
# Importar del core auth de django
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

def validation_email(value):
    print('logica de validacion')
    
def validation_dni(value):
    return

class FormBasicUser(forms.Form):
    # fields
    segundo_nombre = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(validators=[validation_email])
    dni = forms.CharField(max_length=10, validators=[])

class CustomUserCreateForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age',) 

class CustomUserEditForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age',) 