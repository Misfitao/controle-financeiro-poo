from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)    

categoria_receitas = cadastrar_categoria("receitas")
categoria_viagens = cadastrar_categoria("viagens")
categoria_lazer = cadastrar_categoria("lazer")
categoria_contas = cadastrar_categoria("contas fixas")

cadastrar_transacao(
    descricao = "salario abri/2025",
    valor = 1000.0,
    categoria=categoria_receitas,
)

cadastrar_transacao(
    descricao = "mesada abri/2025",
    valor = 50.0,
    categoria=categoria_receitas,
)

cadastrar_transacao(
    descricao = "ingresso/2025",
    valor = -150.0,
    categoria=categoria_lazer,
)

cadastrar_transacao(
    descricao = "conta de luz",
    valor = -100.0,
    categoria=categoria_contas,
)

cadastrar_transacao(
    descricao = "internet",
    valor = -100.0,
    categoria=categoria_contas,
)

total = saldo_total()

print("saldo total: ", total)