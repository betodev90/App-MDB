from django import forms
from .models import Client, Order

def isCedula(value):
    """Algoritmo para validar la cédula """
    cont = 0
    try:
        if value[2] < "6" and len(value) == 10 and (int(value[0]+value[1]) < 25):
            valores = [int(value[x]) * (2 - x % 2) for x in range(9)]
            suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
            num = int(str(suma)[-1:])
            if num == 0:
                dig_veri = 0
                if int(value[9]) == dig_veri or int(value[9]) == 0:
                    cont += 1
                else:
                    cont = 0
            else:
                dig_veri = 10-num
                if int(value[9]) == dig_veri or int(value[9]) == 0:
                    cont += 1
                else:
                    cont = 0
        else:
            cont = 0
    except:
        cont = 0

    if cont == 0:
        return False
    else:
        return True

class SimpleFormClient(forms.Form):
    dni = forms.CharField(max_length=10, validators=[isCedula])
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        print('validando el dni: ', dni)
        if isCedula(dni):
            return dni
        raise forms.ValidationError("Debe ingresar un No. de cédula válido!")


class ModelFormClient(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
    
    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if isCedula(dni):
            return dni
        raise forms.ValidationError("Debe ingresar un No. de cédula válido!")

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['client', 'code']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })