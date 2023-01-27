# Desafio-backend
Interface web que aceita upload de arquivo CNAB, normaliza os dados e armazena-os em um banco de dados relacional, exibindo as informações em tela. A aplicação mostra transações realizadas por lojas e o saldo final de cada uma.

## Linguagem e Tecnologias utilizadas no Projeto
* Python
* Framework Django
* SQlite3
* Views com Django Rest Framework
* ORM do Django
* Serializers
* Templates Django
* HTML
* CSS

## Instalação

**1. Faça o clone do repositório:**

`git clone git@github.com:cirocativo/desafio-backend.git`

**2. Crie e ative o ambiente virtual**

Na pasta do seu repositório, digite os seguintes comandos:

```
python -m venv venv
source venv/bin/activate
```

**3. Instale todos os pacotes necessários para a aplicação funcionar corretamente**

`pip install -r requirements.txt`

**4. Rode as migrações para criação do banco de dados**

`python manage.py migrate`




## Funcionamento

**Execute o comando abaixo para iniciar o servidor**

`python manage.py runserver`

Existem duas URL's disponíveis para acesso:

1. **http://127.0.0.1:8000/transactions/upload/** - para fazer upload do arquivo CNAB
2. **http://127.0.0.1:8000/transactions/show/** - para ver as informações guardadas no banco provenientes de todos os arquivos CNAB que já foram enviados. As informações são organizadas por loja.

No repositório há um exemplo de arquivo CNAB (cnab_example.txt). Ele deve seguir conforme a estrutura abaixo:

![cnab documentation](https://github.com/cirocativo/desafio-backend/blob/master/assets/cnab_documentation.png)
