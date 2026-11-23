catalogo = {
    "macaxeira": 5.20,  # preço do Kg
    "malancia": 3.50,   # preço do Kg
    "rapadura": 2.50,   # preço do Kg
}


# Exibir catálogo Antonio Salatiel
def mostrar_produtos():
    print("\n" + "=" * 35)
    print("       CATÁLOGO DE PRODUTOS")
    print("=" * 35)
    for produto, preco in catalogo.items():
        print(f"{produto.capitalize():<20} R$ {preco:.2f}/Kg")
    print("=" * 35)


# Adicionar ao carrinho - Thyago Silva
class Carrinho:
    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.itens = {}  # produto -> quantidade em Kg

    def adicionar_produto(self):
        mostrar_produtos()
        nome = input("\nDigite o nome do produto: ").strip().lower()

        if nome not in self.catalogo:
            print("Produto não encontrado!")
            return

        try:
            quantidade = float(
                input("Digite a quantidade em Kg: ").replace(",", ".")
            )
        except ValueError:
            print("Quantidade inválida! Digite um número.")
            return

        if quantidade <= 0:
            print("Digite uma quantidade maior que zero.")
            return

        self.itens[nome] = self.itens.get(nome, 0) + quantidade
        subtotal = self.catalogo[nome] * quantidade
        print(f"{quantidade:.2f} Kg de {nome} adicionado ao carrinho!")
        print(f"Subtotal desse item: R$ {subtotal:.2f}")

    def obter_subtotais(self):
        return {p: q * self.catalogo[p] for p, q in self.itens.items()}

    def mostrar_carrinho(self):
        if not self.itens:
            print("\nCarrinho vazio.")
            return
        print("\n" + "=" * 45)
        print("              SEU CARRINHO")
        print("=" * 45)
        for produto, qtd in self.itens.items():
            sub = qtd * self.catalogo[produto]
            print(f"{produto.capitalize():<15} {qtd:>6.2f} Kg   R$ {sub:>7.2f}")
        print("-" * 45)
        print(f"{'TOTAL':<15} {'':>10}   R$ {somar_valores(self.obter_subtotais()):>7.2f}")
        print("=" * 45)


# Soma dos valores - Eduardo Moraes
def somar_valores(subtotais):
    #Retorna o total da compra somando os subtotais.
    return round(sum(subtotais.values()), 2)


# Finalizar compra - Amanda Vieira
def finalizar_compra(total):
    #Solicita o pagamento em dinheiro e exibe o troco.
    print(f"\nTotal a pagar: R$ {total:.2f}")
    while True:
        try:
            entrada = input("Valor pago em dinheiro (R$): ").replace(",", ".")
            valor_pago = float(entrada)
        except ValueError:
            print("Valor inválido! Digite um valor numérico.")
            continue

        if valor_pago <= 0:
            print("Digite um valor maior que zero.")
            continue

        if valor_pago < total:
            print(f"Valor insuficiente! Faltam R$ {total - valor_pago:.2f}.")
            continue

        troco = valor_pago - total
        print("-" * 45)
        print(f"Valor recebido: R$ {valor_pago:.2f}")
        print(f"Troco         : R$ {troco:.2f}")
        print("=" * 45)
        print("Venda concluída com sucesso! Volte sempre.")
        break


# Menu principal
def iniciar_pdv():
    carrinho = Carrinho(catalogo)

    while True:
        print("\n===== PDV =====")
        print("1 - Ver catálogo")
        print("2 - Adicionar produto")
        print("3 - Ver carrinho")
        print("4 - Finalizar compra")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            mostrar_produtos()
        elif opcao == "2":
            carrinho.adicionar_produto()
        elif opcao == "3":
            carrinho.mostrar_carrinho()
        elif opcao == "4":
            total = somar_valores(carrinho.obter_subtotais())
            if total == 0:
                print("Carrinho vazio! Adicione produtos primeiro.")
                continue
            carrinho.mostrar_carrinho()
            finalizar_compra(total)
            break
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    iniciar_pdv()
