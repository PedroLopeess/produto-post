from db import db                       # DE db IMPORTAR db: importa a instância do SQLAlchemy que gerencia o banco de dados

class Produto(db.Model):                   # Define a classe produto como um modelo do SQLAlchemy (herda de db.Model)
    __tablename__ = 'produtos'              # Nome da tabela no banco de dados será "carros"

    id = db.Column(db.Integer, primary_key=True)          # Coluna "id": número inteiro, chave primária (identificador único)
    nome = db.Column(db.String(80), nullable=False)     # Coluna "modelo": texto com limite de 80 caracteres, não pode ser nula
    categoria = db.Column(db.String(80), nullable=False)      # Coluna "marca": texto com limite de 80 caracteres, não pode ser nula
    preço = db.Column(db.Integer, nullable=False)           # Coluna "ano": número inteiro, não pode ser nulo

    def json(self):                                        # Define o método json() que retorna os dados do carro como dicionário
        return {
            'id': self.id,            # Retorna o ID do carro
            'nome': self.nome,    # Retorna o modelo do carro
            'categoria': self.categoria,      # Retorna a marca do carro
            'preço': self.preço           # Retorna o ano do carro
        }
