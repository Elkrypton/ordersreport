from django import forms
import pyqrcode
from django import forms
from .models import Manufacturer
class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ['vendor', 'model', 'store_sku', 'omsid', 'store_so_sku', 'parts_usage']
        widgets = {
            'vendor': forms.TextInput(attrs={'size':'40', 'class': 'form-control'}),
            'model': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'store_sku': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'omsid': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'store_so_sku': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'parts_usage': forms.TextInput(attrs={'size':'40','class': 'form-control'})}
    
