from flask_sqlalchemy import SQLAlchemy   # DE flask_sqlalchemy IMPORTAR SQLAlchemy:
                                          # Extensão do Flask que integra o ORM SQLAlchemy para manipular bancos de dados

db = SQLAlchemy()                         # Cria uma instância do SQLAlchemy (objeto que gerencia a conexão, tabelas e sessões do banco)
