import requests
ced = 58052238
dados_do_cep = {"cep" : cep, "lagradouro": "", "complemento": "", "bairro": "", "localidade": "", "uf": "", "ibge": "", "gia": "", "ddd": "", "siafi": ""}

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        dados_do_cep = dados_da_api = response.json()
        return dados_do_cep
    else:
        return None
    
    print(buscar_cep(cep))