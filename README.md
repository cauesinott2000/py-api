# API

Essa API foi feita em Phython com a biblioteca FastAPI, que permite criar APIs RESTful com facilidade.

## RECURSOS E VANTAGENS DA BIBLIOTECA INCLUEM:
> Alta performance, permitindo que as suas APIs lidem com excesso de requisições de maneira rápida e eficiente.
> Além disso, o FastAPI também é completamente baseado em Python, o que o torna fácil de aprender e integrar com outras bibliotecas Python.
> Outra vantagem é a sua documentação automática, que permite que os usuários da sua API possam entender facilmente como ela funciona e como usá-la.

Para instalar a biblioteca utiliza-se o gerenciador de pacotes do Python, o pip.
**Recomendação:** criar o projeto dentro de um ambiente virtual, para não bagunçar as bibliotecas de outros projetos. (_virtualenv_)

Instalação (no terminal do venv): `pip install fastapi uvicorn`
Exemplo:
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello world, FastAPI!"}
```

## Informações úteis
[Socket Programming in Python (Guide) - Real Python](https://realpython.com/python-sockets/);
[socket - Low-level networking interface - Python 3.11.4 documentation](https://docs.python.org/3/library/socket.html);
[FastAPI - Home](https://fastapi.tiangolo.com/);
[Tutorial - User Guide - FastAPI](https://fastapi.tiangolo.com/tutorial/).
