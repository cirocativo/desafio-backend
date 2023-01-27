# desafio-backend
interface web que aceita upload do arquivo CNAB, normaliza os dados e armazena-os em um banco de dados relacional e exibe essas informações em tela.

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

**5. Execute o comando para iniciar o servidor**

`python manage.py runserver`



## Funcionamento

Existem duas URL's disponíveis para acesso:

1. **http://127.0.0.1:8000/transactions/upload/** - para fazer upload do arquivo CNAB
2. **http://127.0.0.1:8000/transactions/show/** - para ver as informações guardadas no banco provenientes de todos os arquivos CNAB que já foram enviados.

No repositório há um arquivo exemplo de arquivo CNAB (cnab_example.txt). Ele deve seguir a seguinte estrutura:
