from django import forms

class MyForm(forms.Form):
    manufacturer = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'manufacturer','style':'width:300px;'}))
    model = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'model','style':'width:300px;'}))
    store_sku = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'SKU Number','style':'width:300px;'}))
    omsid = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'OMSID','style':'width:300px;'}))
    store_so_sku = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'store SO Number','style':'width:300px;'}))
    parts_usage = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Parts Usage','style':'width:300px;'}))

