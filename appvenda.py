catalogo = {
    "macaxeira": 5.20, #preço do Kg
    "malancia": 3.50, #preço do Kg
    "rapadura": 2.50 #preço do Kg
}

carrinho = {}

#Exibir catalogo Antonio Salatiel
#Adicionar ao carrinho # Thyago Silva
#Soma dos valores Eduardo Moraes
def somar_valores():
    #soma dos valores
    total = 0

    for subtotal in carrinho.values():
        total += subtotal
    return total


#finalizar_compra() Amanda Vieira
 while True:
        try:
            valor_pago = float(input("Valor pago em dinheiro (R$): "))
            if valor_pago < total:
                faltante = total - valor_pago
                print(f"Valor insuficiente! Faltam R$ {faltante:.2f}.")
            else:
                troco = valor_pago - total
                print ("-" * 45)
                print (f"Valor Recebido: R$ {valor_pago:.2f}")
                print (f"Troco  : R$ {troco:.2f}")
                print ("=" * 45)
                print ("Venda concluída com sucesso! Volte sempre.")
                break
        except ValueError:
                print("Valor inválido! Digite um valor numérico.")


if __name__ == "__main__":
    iniciar_pdv()
