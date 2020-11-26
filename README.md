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
BriocheFood é uma aplicação criada para ser um marketplace de padarias, conectando estabelecimentos e clientes de maneira simples e eficiente 🚀. 

* Esta aplicação está em constante evolução e já conta com:

  * Api Restful, pronta para ser consumida: http://127.0.0.1:5000/api/v1/'resource'    
    * Criação de recebedores (padarias parceiras)
    * Diversos recursos disponíveis através de seus endpoits, documentação disponível em: [PAGARME](https://pagar.me/)

  * Integração com a API de pagamentos [PAGARME](https://pagar.me/) para:
    * Criação de recebedores (padarias parceiras)
    * Transações 

  * Painel administrativo
    * Gerenciamento a nível de administrador para as entidades abaixo listadas mediante acesso em http://127.0.0.1:5000/admin/ com as credenciais name=Django e password=Livre<br/>
      * Address<br/>
      * Bakery<br/>
      * Cart<br/>
      * Delivery<br/>
      * Order<br/>
      * Product<br/>
      * Purchase<br/>
      * User

* O que a aplicação ainda não possui:
  * Aplicativo mobile ou website para consumo dos recursos

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

### Pré-requisitos do sistema

Requisitos necessários para executar o projeto e como instalar caso ainda não possua.
* Em sistemas operacionais Linux baseados em Debian (Recomendado Ubuntu 19.04 ou superior):
  ```sh
  sudo apt update
  sudo apt install git
  sudo apt install python3.7
  sudo apt install python3-pip
  ```

### Ambiente Virtual
Ps: Recomenda-se a criação e utilização de um ambiente virtual python previamente definido com a versão python padrão utilizada (python 3.7). 

* Instalação do pacote Virtualenvwrapper<br/>
  Execute:
  ```sh       
    $ pip install virtualenvwrapper
   ```

  Então adicione ao final do arquivo ~/.bash_profile as linhas a seguir:
   ```sh       
    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
   ```

* Criação e uso do ambiente virtual
   ```sh   
   $ mkvirtualenv nome_do_ambiente 
   $ workon nome_do_ambiente --python=/usr/local/bin/python3.7
   
   # Para sair do ambiente virtual
   $ deactivate
  ```

### Instalação
1. Obtenha uma chave API gratuíta em [https://pagar.me/precos/](https://pagar.me/precos/) 
    * Lembre-se de utilizar a chave API de testes.

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
Diagrama de classes simplificado:  [Acessar](https://example.com) <br/>
Endpoits da api disponíveies em: [Acessar](https://pagar.me/)

<!-- USAGE EXAMPLES -->
## Uso
Atente-se ao fato de que para que seja possível realizar uma transação sem a necessidade de informar um usuário é necessário que a sua chave ANTIFRAUDE na plataforma da pagarme esteja desabilitada. 


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



