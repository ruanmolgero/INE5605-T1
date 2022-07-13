from datetime import datetime

from controle.controlador_categoria import ControladorCategoria
from controle.controlador_produto_preco import ControladorProdutoPreco
from controle.controlador_qualificador import ControladorQualificador
from controle.controlador_sistema import ControladorSistema
from controle.controlador_supermercado import ControladorSupermercado
from controle.controlador_usuario import ControladorUsuario

from entidade.categoria import Categoria
from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
from entidade.preco import Preco
from entidade.produto import Produto
from entidade.qualificador import Qualificador
from entidade.supermercado import Supermercado


u1 = PessoaFisica(nome="Ruan Luiz Molgero Lopes", email="ruanmolgero@gmail.com", cpf="070.002.529-44")
u2 = PessoaJuridica(nome="Supermercado Giassi", email="giassi@gmail.com", cnpj="76.904.575/0001-09")
u3 = PessoaJuridica(nome="Supermercado Angeloni", email="angeloni@gmail.com", cnpj="36.121.725/0001-85")

s1 = Supermercado(nome="Giassi", endereco="Rua Afonso Pena", cadastrante=u2)
s2 = Supermercado(nome="Angeloni", endereco="Avenida Max Schram", cadastrante=u3)

c1 = Categoria(nome="Higiene", descricao="Sabonetes, cremes, shampoos, etc")
c2 = Categoria(nome="Açougue", descricao="Carnes, etc")

q1_p1 = Qualificador(titulo="Peso", descricao="200g")
q2_p1 = Qualificador(titulo="Tipo", descricao="Côco")
q3_p1 = Qualificador(titulo="Marca", descricao="Johnsons & Johnsons")
p1 = Produto(nome="Sabonete", descricao="Sabonete", qualificadores=[q1_p1, q2_p1, q3_p1])

q1_p2 = Qualificador(titulo="Peso", descricao="200g")
q2_p2 = Qualificador(titulo="Tipo", descricao="Amêndoas")
q3_p2 = Qualificador(titulo="Marca", descricao="Johnsons & Johnsons")
p2 = Produto(nome="Sabonete", descricao="Sabonete", qualificadores=[q1_p2, q2_p2, q3_p2])

pr1 = Preco(valor=4.57)
pr2 = Preco(valor=6.57)

# pr1 = Preco(valor=4.57, cadastrante=u1)
# pr2 = Preco(valor=6.57, cadastrante=u2)

# print(datetime.now().date())
# print(pr1.data)

# print("Usuários")
# print(u1, u2, u3)

# print("Supermercados")
# print(s1, s2)

# print("Categorias")
# print(c1, c2)

# print("Qualificadores/Produto")
# print(q1_p1, q2_p1, q3_p1, p1)

# print("Qualificadores/Produto")
# print(q1_p2, q2_p2, q3_p2, p2)

# print("Preços")
# print(pr1, pr2)

# Controladores para o sistema
controlador_sistema = ControladorSistema()
controlador_usuario = controlador_sistema.controlador_usuario
controlador_supermercado = controlador_sistema.controlador_supermercado
controlador_categoria = controlador_sistema.controlador_categoria
controlador_qualificador = controlador_sistema.controlador_qualificador
controlador_produto_preco = controlador_sistema.controlador_produto_preco

# Usuários
dados_usuario_fisico = {
    "nome": "Ruan Luiz Molgero Lopes",
    "email": "ruanmolgero@gmail.com",
    "cpf": "070.002.529-44"
}

dados_usuario_juridico = {
    "nome": "Ruan Luiz Juridico",
    "email": "ruanjuridico@gmail.com",
    "cnpj": "76.904.575/0001-09"
}

controlador_sistema.controlador_usuario.criar_usuario(dados=dados_usuario_fisico)
controlador_sistema.controlador_usuario.criar_usuario(dados=dados_usuario_juridico)
print(f"Usuário fisico: {controlador_usuario.achar_usuario_por_cpf(dados_usuario_fisico['cpf'])}")
print(f"Usuário juridico: {controlador_usuario.achar_usuario_por_cnpj(dados_usuario_juridico['cnpj'])}")
print()

# Login
dados_login_fisico = {
    "email": "ruanmolgero@gmail.com",
    "cpf": "070.002.529-44"
}

dados_login_juridico = {
    "email": "ruanjuridico@gmail.com",
    "cnpj": "76.904.575/0001-09"
}

controlador_sistema.controlador_usuario.realizar_login(dados=dados_login_fisico)
print(f"Usuário logado: {controlador_usuario.usuario_logado}")
print()

# Supermercado
dados_supermercado1 = {
    "nome": s1.nome,
    "endereço": s1.endereco,
}

dados_supermercado2 = {
    "nome": s2.nome,
    "endereço": s2.endereco,
}

controlador_sistema.controlador_supermercado.criar_supermercado(dados=dados_supermercado1)
supermercado_selecionado = controlador_supermercado.supermercado_selecionado
print(f"Supermercados: {controlador_supermercado.supermercados}")
print(f"Supermercado selecionado: {supermercado_selecionado}")
print()


# Categoria
dados_categoria1 = {
    "nome": c1.nome,
    "descricao": c1.descricao,
}

dados_categoria2 = {
    "nome": c2.nome,
    "descricao": c2.descricao,
}

controlador_sistema.controlador_categoria.criar_categoria(dados=dados_categoria1)
categoria_selecionada = controlador_categoria.categoria_selecionada
print(f"Categorias do supermercado {supermercado_selecionado}: {supermercado_selecionado.categorias}")
print(f"Categoria selecionada: {categoria_selecionada}")
print()

dados_qualificador1 = {
    "titulo": q1_p1.titulo,
    "descricao": q1_p1.descricao
}

dados_qualificador2 = {
    "titulo": q2_p1.titulo,
    "descricao": q2_p1.descricao
}

dados_qualificador3 = {
    "titulo": q3_p1.titulo,
    "descricao": q3_p1.descricao
}

controlador_sistema.controlador_qualificador.criar_qualificador(dados=dados_qualificador1)
controlador_sistema.controlador_qualificador.criar_qualificador(dados=dados_qualificador2)
controlador_sistema.controlador_qualificador.criar_qualificador(dados=dados_qualificador3)
print(
    f"Qualificadores categoria {controlador_categoria.categoria_selecionada}: {controlador_qualificador.qualificadores}")
print(f"Qualificadores selecionados: {controlador_qualificador.qualificadores_selecionados}")
print()

dados_produto1 = {
    "nome": p1.nome,
    "descricao": p1.descricao,
    "valor": pr1.valor,
}

controlador_sistema.controlador_produto_preco.criar_produto(dados=dados_produto1)
print(f"Produtos: {controlador_produto_preco.produtos}")
print()
print(controlador_produto_preco.produtos[0].nome)
print(controlador_produto_preco.produtos[0].descricao)
print(controlador_produto_preco.produtos[0].qualificadores[0].titulo,
      controlador_produto_preco.produtos[0].qualificadores[0].descricao)
print(controlador_produto_preco.produtos[0].qualificadores[1].titulo,
      controlador_produto_preco.produtos[0].qualificadores[1].descricao)
print(controlador_produto_preco.produtos[0].qualificadores[2].titulo,
      controlador_produto_preco.produtos[0].qualificadores[2].descricao)
print(controlador_produto_preco.produtos[0].precos[0].valor,
      controlador_produto_preco.produtos[0].precos[0].cadastrantes[0].nome,
      controlador_produto_preco.produtos[0].precos[0].contador)
print(controlador_supermercado.supermercados[0].categorias)
