from django import forms
from apps.organizacion.models import Almacen



class AlmacenForm(forms.ModelForm):

    class Meta:
        model = Almacen

        fields = [
            'almacen_id',
            'clave',
            'descripcion',
            'id_domicilio',
            'status',
        ]
        labels = {
            'almacen_id': 'Almacen',
            'clave': 'Clave',
            'descripcion': 'Descripcion',
            'id_domicilio': 'Domicilio',
            'status': 'Estatus',
        }
        widgets = {
            'almacen_id': forms.TextInput(attrs={'class':'forms-control'}),
            'clave': forms.TextInput(attrs={'class':'forms-control'}),
            'descripcion': forms.TextInput(attrs={'class':'forms-control'}),
            'id_domicilio': forms.TextInput(attrs={'class':'forms-control'}),
            'status': forms.TextInput(attrs={'class':'forms-control'}),
        }