from flask import Blueprint, request                  # DE flask IMPORTAR Blueprint e request:
                                                      # - Blueprint: usado para organizar as rotas do Flask em módulos separados
                                                      # - request: objeto que contém os dados enviados na requisição HTTP

from controllers.produto_controllers import create_produto # DE controllers.produto_controllers IMPORTAR create_produto:
                                                      # função que cria um novo produto no banco (controller)

produto_routes = Blueprint('produto_routes', __name__)    # Cria um Blueprint chamado "produto_routes" (identificador),
                                                      # associado ao módulo atual (__name__), para registrar rotas do produto

@produto_routes.route('/produto', methods=['POST'])       # Define a rota "/Produto" que aceita apenas requisições HTTP POST
def produto_post():                                    # Função que será executada quando houver POST em "/Produto"
    produto_data = request.json                         # Lê o corpo da requisição no formato JSON e armazena em produto_data
    return create_produto(request.json)                 # Chama a função create_produto (controller) passando os dados recebidos
