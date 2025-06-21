<div align="center">
    <h1>Sistema Notificações para o SGE</h1>
    <img src="https://img.shields.io/github/repo-size/elainefs/django-sge-notify">
    <img src="https://img.shields.io/github/languages/top/elainefs/django-sge-notify"> 
    <img src="https://img.shields.io/github/last-commit/elainefs/django-sge-notify?color=blue">
    <img src="https://img.shields.io/github/license/elainefs/django-sge-notify.svg?color=blue">
    <br><br>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white">
    <img src="https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white">
</div>

## 📘 Sobre

Sistema de notificações que expõe um endpoint de webhook. Esse sistema de notificações foi desenvolvido para ser usado junto ao [Sistema de Gerenciamento de Estoque (SGE)](https://github.com/elainefs/django-sge) para o disparo de notificações por e-mail e WhatsApp via API do [CallMeBot](https://www.callmebot.com/) quando ocorrem movimentações de saída no estoque.

## 💻️ Tecnologias

- Python
- Django
- Django REST Framework
- SQLite

## ⚙️ Como usar

Para executar essa aplicação siga os seguintes passos:

1. Clone o repositório

```bash
git clone https://github.com/elainefs/django-sge-notify.git
```

2. Crie e ative um ambiente virtual

```bash
python3 -m venv .venv # Para Windows use: python -m venv .venv

source .venv/bin/activate  # Para Windows use: .venv\Scripts\activate
```

3. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto

O arquivo `.env.example` é um modelo de como o seu arquivo `.env` deve ser.

Para gerar uma nova `SECRET_KEY`, a partir da raiz do projeto, use o seguinte comando no terminal:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Além da nova `SECRET_KEY` que você deve adicionar à `.env` é necessário configurar a API do CallMeBot, você deve fazer o processo descrito no site da API para obter sua própria API KEY e adicionar as informações nas seguintes variáveis na `.env`:

```
CALLMEBOT_API_URL
CALLMEBOT_PHONE_NUMBER
CALLMEBOT_API_KEY
```

5. Execute as migrações no banco de dados

Esse sistema utiliza o SQLite como banco de dados.

```bash
python3 manage.py migrate
```

6. Crie um super usuário

```bash
python3 manage.py createsuperuser
```

7. Execute a aplicação

Para que o disparo de notificações ocorra de forma adequada o SGE e a aplicação de notificações devem estar em execução simultaneamente.

O SGE é configurado para ser executado por padrão na porta 8000, então execute a aplicação de notificações em outra porta, no exemplo abaixo a aplicação está sendo executada na porta 8001.

```bash
python3 manage.py runserver 8001
```

Além disso, lembre-se de configurar a `.env` do projeto SGE, a variável `NOTIFICATION_URL` deve receber a URL em que a aplicação de notificações está sendo executada.

O gerenciamento das notificações pode ser feito através da interface do Django Admin em: `http://localhost:8001/admin/`

## 📝 Mensagens de Notificações

A aplicação dispara notificações via e-mail e via WhatsApp.

A mensagem enviada via e-mail usa uma estrutura em HTML, ela está localizada em `webhooks/templates/outflow.html`.

A mensagem enviada via WhatsApp está localizada em `webhooks/messages.py`.

As variáveis que preenchem dinamicamente as mensagens são configuradas em `webhooks/views.py`

## 📄 Licença

Este projeto está sobre a licença MIT. Veja o arquivo [LICENSE](https://github.com/elainefs/django-sge-notify/blob/main/LICENSE) para mais informações.

---

Made with <3 by [Elaine Ferreira](https://github.com/elainefs/)
