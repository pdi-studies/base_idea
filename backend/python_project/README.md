# Projeto Python

Projeto desenvolvido para estudo da linguagem Python


### Executando ambos os projetos

Na raiz do projeto execute os comandos:

Cria ambiente virtual:

```bash
python3 -m venv python_project
```
Ativa o ambiente virtual:

Windows:
```bash
.\venv\Scripts\activate
```

Linux / mac:
```bash
source venv/bin/activate
```

Instala das dependências e inicia o projeto
```bash
pip  install  --no-cache-dir  -r  requirements.txt
python  app.py
```

Para realizar os testes de integração
```bash
python -m unittest tests.test_categories
```
 
Ao executar o comando ele irá subir a aplicação Python, além de criar a tabela 'categories' e popular a mesma com os dados necessários que estão na categories.csv.

#### Swagger
  
[http://localhost:5000/apidoc/swagger#/](http://localhost:5000/apidoc/swagger#/)
 

#### Endpoints
  
- API RESTful que pega os dados das categorias de pets:

- Acesse a API GET: [http://localhost:5000/api/categories/](http://localhost:5000/api/categories/)