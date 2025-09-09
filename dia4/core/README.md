# 📦 Workshop Back-End Turma 2 — 2025.2

Este projeto foi desenvolvido como parte do workshop de Back-End da Turma 2 (2025.2), utilizando o framework **Django**. O objetivo principal é permitir que o usuário consulte um endereço completo informando apenas o **CEP**, com preenchimento automático dos campos via integração com a API [ViaCEP](https://viacep.com.br).

---

## 🚀 Funcionalidades

- Consulta de endereço por CEP
- Integração com a API ViaCEP
- Preenchimento automático dos campos de endereço
- Interface simples e funcional
- Estrutura modular com múltiplos apps Django

---

## 🛠️ Tecnologias utilizadas

- Python 3.13
- Django 5.2
- HTML5
- CSS (opcional para estilização)
- API ViaCEP
- Git & GitHub

---

## 📂 Estrutura do projeto

WorkshopBack-End-Turma2-2025.2/ ├── meuprojeto/
 # Configurações principais do Django │ └── urls.py │ └── settings.py ├── dia4/ │ └── core/ # App principal de consulta de endereço │ ├── models.py │ ├── views.py │ ├── forms.py │ ├── urls.py │ └── templates/ │ └── home.html ├── primeiro_app/ # App complementar ├── app2/ # Outro app complementar └── manage.py

Código

---

## 📋 Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/LeviAdler05/WorkshopBack-End-Turma2-2025.2.git
   cd WorkshopBack-End-Turma2-2025.2
Crie e ative um ambiente virtual:

bash
python -m venv venv
venv\Scripts\activate  # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Execute as migrações:

bash
python manage.py makemigrations
python manage.py migrate
Inicie o servidor:

bash
python manage.py runserver
Acesse no navegador:

Código
http://127.0.0.1:8000/core/
🧠 Observações
A verificação SSL foi desativada temporariamente para evitar conflitos com certificados locais. Para produção, recomenda-se configurar um certificado confiável.

O projeto está estruturado para facilitar a expansão com novos apps e funcionalidades.


👨‍💻 Autor
Desenvolvido por Levi Adler 📧 leviadler05@gmail.com 🔗 GitHub: LeviAdler05