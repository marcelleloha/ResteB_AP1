# Catálogo de Produtos API - AP1

Este projeto é uma API RESTful desenvolvida com **Django** e **Django REST Framework**, projetada para gerenciar produtos e suas respectivas lojas. O projeto foi configurado para ser executado localmente e implantado na **AWS Elastic Beanstalk**.

**Link da API Publicada:** [http://catalogo-produtos-env.eba-3xd3cama.us-east-1.elasticbeanstalk.com/api](http://catalogo-produtos-env.eba-3xd3cama.us-east-1.elasticbeanstalk.com/api)

---

## Integrantes do Grupo
* Bryan Amorim dos Santos
* Gustavo Salvador
* Julia Curto
* 
*
*

---

## Alterações Realizadas

Criamos uma nova classe `Loja` que se relaciona com a classe já existente `Produto`:

1.  **Nova Classe `Loja`:** Criada para armazenar informações sobre os estabelecimentos, incluindo nome, localização e bairro.
2.  **Relacionamento:** A classe `Produto` foi alterada para incluir um relacionamento de chave estrangeira (`ForeignKey`) com a classe `Loja`, permitindo que cada produto seja vinculado a uma loja específica.
3.  **Atualização de APIs:** Foram criados novos Serializers, Viewsets e Rotas para suportar operações CRUD completas tanto para produtos quanto para lojas.

---

## Configuração e Execução Local

### Pré-requisitos
* Python 3.12 instalado.
* Git instalado.

### Passo a Passo
1.  **Clonar o repositório:**
    ```bash
    git clone [URL_DO_REPOSITORIO]
    cd ResteB_AP1
    ```
2.  **Criar e ativar o ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
    ```
3.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Executar Migrações:**
    ```bash
    python manage.py migrate
    ```
5.  **Iniciar o servidor:**
    ```bash
    python manage.py runserver
    ```
A API estará disponível em `http://127.0.0.1:8000/api`.

---

## Implementação e Deploy na AWS

O deploy foi realizado utilizando o **AWS Elastic Beanstalk** com o empacotamento em arquivo `app.zip`. As seguintes etapas foram seguidas:

1.  **Configurações de Ambiente (`.ebextensions`):**
    * O arquivo `django.config` foi configurado para automatizar as migrações (`migrate`), coleta de estáticos (`collectstatic`) e permissões de escrita no banco SQLite no servidor AWS.
    * A plataforma foi definida como **Python 3.12**.
2.  **Servidor de Produção:** Utilização do **Gunicorn** configurado no arquivo `Procfile` para gerenciar as requisições HTTP na porta 8000.
3.  **Empacotamento:** Criação do arquivo `app.zip` contendo as pastas `catalogo`, `produtos`, arquivos de configuração e o arquivo `manage.py`.

