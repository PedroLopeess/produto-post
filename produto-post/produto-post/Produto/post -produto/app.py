from flask import Flask                                  # DE flask IMPORTAR Flask: classe principal usada para criar a aplicação web
from db import db                                        # DE db IMPORTAR db: instância do SQLAlchemy que gerencia a conexão com o banco
from routes.carro_routes import carro_routes             # DE routes.carro_routes IMPORTAR carro_routes: conjunto de rotas do módulo carro

app = Flask(__name__)                                    # Cria a aplicação Flask, passando __name__ para identificar o módulo principal
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carros.db'  # Configuração: URL de conexão com o banco de dados SQLite chamado carros.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     # Desativa rastreamento extra de modificações (melhora performance e evita warnings)
db.init_app(app)                                         # Inicializa a extensão SQLAlchemy com a aplicação Flask

app.register_blueprint(carro_routes)                     # Registra o blueprint das rotas de carro na aplicação

if __name__ == '__main__':                               # Garante que o código abaixo só será executado se rodar diretamente este arquivo
    with app.app_context():                              # Cria um contexto da aplicação (necessário para acessar recursos do Flask)
        db.create_all()                                  # Cria todas as tabelas do banco de dados conforme os modelos definidos
    app.run(debug=True)                                  # Inicia o servidor Flask em modo debug (atualiza automaticamente ao alterar código)
