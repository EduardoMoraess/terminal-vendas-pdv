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
