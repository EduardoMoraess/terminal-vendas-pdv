# Cores ANSI
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
CIANO = "\033[36m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

catalogo = {
    "macaxeira": 5.20,  # preço do Kg
    "melancia": 3.50,   # preço do Kg
    "rapadura": 2.50    # preço do Kg
}

# Carrinho de compras
carrinho = {}

# Exibir catálogo
def exibir_catalogo():
    print(f'\n{AMARELO}{NEGRITO}--- Produtos Disponíveis ---{RESET}')

    for produto, preco in catalogo.items():
        print(f'{CIANO}{produto.title()}{RESET} - {VERDE}R${preco:.2f}{RESET}')

# Adicionar produto ao carrinho
def adicionar_carrinho():
    produto = input(f'{CIANO}Digite o nome do produto:=> {RESET}').lower()

    if produto in catalogo:
        quantidade = int(input(f'{CIANO}Quantidade:=> {RESET}'))

        if quantidade > 0:
            if produto in carrinho:
                carrinho[produto] += quantidade
            else:
                carrinho[produto] = quantidade
            subtotal = catalogo[produto] * quantidade
            print(f'{AMARELO}Subtotal R${subtotal:.2f}{RESET}')
            print(f'{VERDE}Produto adicionado!{RESET}')
        else:
            print(f'{VERMELHO}Quantidade inválida{RESET}')
    else:
        print(f'{VERMELHO}Produto não encontrado no sistema!{RESET}')

# Calcular total
def calculo_total():
    total = 0
    for produto, quantidade in carrinho.items():
        total += catalogo[produto] * quantidade
    return total

# Finalizar compra
def finalizar_compra():
    print(f'\n{AMARELO}{NEGRITO}--- Resumo da Compra ---{RESET}')

    for produto, quantidade in carrinho.items():
        subtotal = catalogo[produto] * quantidade
        print(f'{CIANO}{produto.title()}{RESET} x {quantidade} = {VERDE}R${subtotal:.2f}{RESET}')

    total = calculo_total()

    print(f'\n{NEGRITO}{VERDE}TOTAL R${total:.2f}{RESET}')

    if total > 0:
        pagamento = float(input(f'{CIANO}Valor pago: {RESET}'))

        if pagamento >= total:
            troco = pagamento - total
            print(f'{AMARELO}TROCO R${troco:.2f}{RESET}')
            print(f'{VERDE}{NEGRITO}Compra finalizada!{RESET}')
        else:
            falta = total - pagamento
            print(f'{VERMELHO}Valor insuficiente, faltam R${falta:.2f}{RESET}')
    else:
        print(f'{VERMELHO}CARRINHO VAZIO!{RESET}')

# Programa principal
print(f'{NEGRITO}{AMARELO}=== FEIRA DA AGRICULTURA FAMILIAR ==={RESET}')

exibir_catalogo()

while True:
    opcao = input(f'\n{CIANO}Digite 1 para comprar ou "finalizar":=> {RESET}').lower().strip()

    if opcao == '1':
        adicionar_carrinho()
    elif opcao == 'finalizar':
        finalizar_compra()
        break
    else:
        print(f'{VERMELHO}Opção inválida, tente novamente{RESET}')

print(f'\n{VERDE}Obrigado pela preferência!{RESET}')
