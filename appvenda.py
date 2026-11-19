#Exibir catalogo Antonio Salatiel
#Adicionar ao carrinho
#Soma dos valores Eduardo Moraes
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
