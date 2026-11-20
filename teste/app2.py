catalogo = {
    "macaxeira": 5.20, #preço do Kg
    "malancia": 3.50, #preço do Kg
    "rapadura": 2.50 #preço do Kg
}

carrinho = {}

def exibir_catalogo():
    print('\n---Produtos Disponiveis---')

    for produto, preco in catalogo.items():
        print(f'{produto.title()} - R${preco:.2f}')

def adicionar_carrinho():
    produto = input('Digite nome do produto:=>').lower()

    if produto in catalogo:
        quantidade = int(input('Quantidade:=>'))

        if quantidade == 0:
            if produto in catalogo:
                carrinho[produto] += quantidade
            else:
                carrinho[produto] = quantidade
            subtotal = catalogo[produto]*quantidade
            print(f'Subtotal R${subtotal:.2f}')
            print('Produto adicionado')
        else:
            print('Quantidade invalida')
    else:
        print('Produto não encontrado no sistema!')
