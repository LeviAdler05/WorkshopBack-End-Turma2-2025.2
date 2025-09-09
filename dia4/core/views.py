from django.shortcuts import render
from .models import Endereco
from .forms import EnderecoForm
import requests

def consultar_enderecos(request):
    endereco = None

    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            cep = form.cleaned_data['cep']
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", verify=False)
            if response.status_code == 200:
                dados = response.json()
                endereco = Endereco(
                    cep=dados.get('cep', ''),
                    logradouro=dados.get('logradouro', ''),
                    complemento=dados.get('complemento', ''),
                    bairro=dados.get('bairro', ''),
                    localidade=dados.get('localidade', ''),
                    uf=dados.get('uf', ''),
                    ibge=dados.get('ibge', ''),
                    gia=dados.get('gia', ''),
                    ddd=dados.get('ddd', ''),
                    siafi=dados.get('siafi', '')
                )
    else:
        form = EnderecoForm()

    return render(request, 'home.html', {
        'form': form,
        'endereco': endereco
    })
