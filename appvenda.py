#catalogo

catalogo = {
    "macaxeira": 3.50, # precço do KG
    "rapadura": 5.00
}

carrinho = {}

#função para mostrar os produtos
def mostrar_produtos():
    print("\n---Produtos Disponiveis---")

    for produto, preco in catalogo.items():
        print(f"{produto.title()} - R${preco:.2f}")
