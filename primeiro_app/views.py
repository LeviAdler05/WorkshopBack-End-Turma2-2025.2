from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def hello_world(request):

    agora = timezone.now()
    mensagem = f"""
    <html>
    <head>
        <title>Hello World - Django</title>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f0f0f0;
            }}
            .container {{
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: 0 auto;
            }}
            h1 {{
                color: #2c3e50;
                font-size: 2.5em;
                margin-bottom: 20px;
            }}
            p {{
                color: #7f8c8d;
                font-size: 1.2em;
                margin: 10px 0;
            }}

        </style>
    </head>
    <body>
        <div class="container">
            <h1>Olá Mundo!</h1>
            <p><strong>Data e Hora Atual:</strong> {agora.strftime('%d/%m/%Y às %H:%M:%S')}</p>
            <p><strong>Fuso Horário:</strong> {timezone.get_current_timezone_name()}</p>
            <p><strong>Idioma Configurado:</strong> Português (Brasil)</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(mensagem)
