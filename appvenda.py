catalogo = {
    "macaxeira": 5.20, #preço do Kg
    "malancia": 3.50, #preço do Kg
    "rapadura": 2.50 #preço do Kg
}

carrinho = {}

#Exibir catalogo Antonio Salatiel
#Adicionar ao carrinho # Thyago Silva
#Soma dos valores Eduardo Moraes
def somar_valores(carrinho):
    """Retorna o total da compra somando os subtotais do carrinho."""
    return round(sum(carrinho.values()), 2)


#finalizar_compra() Amanda Vieira

def finalizar_compra(total):
    #Solicita o pagamento em dinheiro e exibe o troco.
    while True:
        try:
            entrada = input("Valor pago em dinheiro (R$): ").replace(",", ".")
            valor_pago = float(entrada)

            if valor_pago <= 0:
                print("Digite um valor maior que zero.")
                continue

            if valor_pago < total:
                print(f"Valor insuficiente! Faltam R$ {total - valor_pago:.2f}.")
                continue

            troco = valor_pago - total
            print("-" * 45)
            print(f"Valor Recebido: R$ {valor_pago:.2f}")
            print(f"Troco         : R$ {troco:.2f}")
            print("=" * 45)
            print("Venda concluída com sucesso! Volte sempre.")
            break

        except ValueError:
            print("Valor inválido! Digite um valor numérico.")


if __name__ == "__main__":
    iniciar_pdv()
