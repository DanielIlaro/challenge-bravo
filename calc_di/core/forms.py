from django import forms

class ListNumbers(forms.Form):
    
    number_numbers = forms.IntegerField(min_value=1, label="Quantidade de números")
    list_numbers = forms.CharField(min_length=1, label="Lista com Números")