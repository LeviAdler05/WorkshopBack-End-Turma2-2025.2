from django import forms
from .models import Endereco
import requests

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep']

    def clean(self):
        cleaned_data = super().clean()
        cep = cleaned_data.get('cep')
        if cep:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", verify=False)
            if response.status_code == 200:
                dados = response.json()
                for campo in ['logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'ddd']:
                    cleaned_data[campo] = dados.get(campo, '')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        cleaned_data = self.cleaned_data
        for campo in ['logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'ddd']:
            setattr(instance, campo, cleaned_data.get(campo, ''))
        if commit:
            instance.save()
        return instance