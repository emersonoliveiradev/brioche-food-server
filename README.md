<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emersonoliveiradev/brioche-food-server">
    <img src="briochefood/assets/images/pao.png" alt="Logo" width="150" height="80">
  </a>

  <h3 align="center">BriocheFood</h3>

  <p align="center">
    Quer saborear aquele pão quentinho feito nas principais padarias da sua cidade? Experimente agora a solução BriocheFood e receba em casa, no trabalho ou em qualquer lugar a sua delícia panificada.
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## Sobre o projeto
BriocheFood é uma aplicação criada para ser um marketplace de padarias, conectando estabelecimentos e clientes de maneira simples e eficiente 🚀. Esta aplicação ainda em desenvolvimento, já conta com:
* Integração com a API de pagamentos [PAGARME](https://pagar.me/)
* Painel administrativo
* Api Restful 

### Construído com
Principais tecnologias utilizadas:

* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [dynaconf](https://dynaconf.readthedocs.io/en/docs_223/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/)
* [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)
* [Flask-SimpleLogin](https://flask-simple-login.readthedocs.io/en/latest/?badge=latest)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)


<!-- GETTING STARTED -->
## Começando

Este é um exemplo de como você pode configurar seu projeto localmente. Para obter uma cópia local instalada e funcionando, siga os passos:

### Pré-requisitos

Requisitos necessários precisa para usar o software e como instalá-las.
* Em sistemas operacionais Linux baseados em Debian (Recomendado Ubuntu 19.04 ou superior):
  ```sh
  sudo apt update
  sudo apt install python3.7
  sudo apt install python3-pip
  ```

### Ambiente Virtual
Ps: Recomenda-se a criação e utilização de um ambiente virtual python previamente definido com a versão python padrão utilizada (python 3.7). 

* Instalação do pacote Virtualenvwrapper<br/>
  
  Adicione ao final do arquivo ~/.bash_profile as linhas a seguir:
   ```sh   
    pip install virtualenvwrapper
    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
   ```

* Criação e utilização do ambiente virtual
   ```sh   
   mkvirtualenv nome_do_ambiente 
   workon nome_do_ambiente --python=/usr/local/bin/python3.7
   
   # Para sair do ambiente virtual
   deactivate
  ```

### Instalação
1. Obtenha uma chave API gratuíta em [https://pagar.me/precos/](https://pagar.me/precos/)

2. Clone o repositório
   ```sh
   $ git clone https://github.com/emersonoliveiradev/brioche-food-server.git
   $ cd brioche-food-server
   ```
3. Instale os pacotes via pip
   ```sh
   $ pip install > requirements.txt
   ```
4. Insira sua chave API em `settings.toml`
   ```JS
   PAGARME_API_KEY = 'Sua Chave API';
   ```

### Execução
1. Execute o comando de criação do banco de dados:
   ```sh
   $ flask create-db
   ```

2. Execute a inicialização do servidor:
   ```sh
   $ flask run
   ```

* Neste momento a aplicação já deverá estar sendo executada em:
  http://127.0.0.1:5000/

### Comandos adicionais
* Considere conferir alguns comandos disponíveis com o comando flask --help 
   ```sh
   $ flask --help   
   create-db    Creates database
   db           Perform database migrations.
   drop-db      Cleans database
   populate-db  Populate db with sample data
   routes       Show the routes for the app.
   run          Run a development server.
   shell        Run a shell in the app context.
   ```
  * Especialmente para criação de uma base de dados simples através do comando:
  ```sh
   $ flask populate-db
   ```

<!-- ADITIONAL DOCUMENTATION -->
## Documentação adicional
Dicionário de dados:  [Acessar](https://example.com) <br/>
Diagrama de classes:  [Acessar](https://example.com) <br/>

<!-- USAGE EXAMPLES -->
## Uso
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.


<!-- CONTRIBUTING -->
## Contribuindo

Caso queira contribuir com este projeto basta seguir as instruções abaixo:

1. Crie um Fork do projeto
2. Crie sua Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Envia sua Branch (`git push origin feature/AmazingFeature`)
5. Abra uma Pull Request



<!-- LICENSE -->
## Licença
Distribuído sobre a licença MIT . 



<!-- CONTACT -->
## Contato
Link do projeto: [https://github.com/emersonoliveiradev/brioche-food-server](https://github.com/emersonoliveiradev/brioche-food-server)

<p align="left">
  <a href="mailto:emersonoliveiradev@gmail.com" alt="Gmail">
    <img src="https://img.shields.io/badge/-emersonoliveiradev@gmail.com-e34c41?style=flat-square&labelColor=e34c41&logo=gmail&logoColor=white&link=emersonoliveiradev@gmail.com</a>" /></a>
   
  <a href="https://www.linkedin.com/in/emerson-oliveira-4582b9123/" alt="Linkedin">
<img src="https://img.shields.io/badge/-Emerson%20Oliveira-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/emerson-oliveira-4582b9123/" /></a>

</p>



