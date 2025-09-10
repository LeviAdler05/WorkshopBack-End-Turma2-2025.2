CRUD de Endereços com Django e ViaCEP

Este projeto é um CRUD completo de endereços com consulta automática via CEP, utilizando Django e a API do ViaCEP.

🚀 Funcionalidades

Consulta de endereço via CEP com preenchimento automático

Criação, listagem, visualização e exclusão de endereços

Templates com herança de layout base

Navegação entre páginas com links

🧱 Estrutura do App viacep

dia5/
└── viacep/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── apps.py
    └── templates/
        └── viacep/
            ├── base.html
            ├── endereco_form.html
            ├── endereco_list.html
            ├── endereco_detail.html
            ├── endereco_confirm_delete.html

⚙️ Configuração

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

Instale as dependências:

pip install django requests

Execute as migrações:

python manage.py makemigrations
python manage.py migrate

Inicie o servidor:

python manage.py runserver

Acesse: http://127.0.0.1:8000/viacep/

📁 Organização do Projeto

dia5.viacep: App principal com modelo, formulário, views e templates

meuprojeto: Projeto Django com configurações e roteamento

🧪 Testes

Você pode adicionar testes automatizados com pytest ou unittest para garantir a estabilidade do sistema.

📦 Requisitos

Python 3.10+

Django 5.2.6

requests

🧑‍💻 Autor

Desenvolvido por Levi durante os estudos com Django.