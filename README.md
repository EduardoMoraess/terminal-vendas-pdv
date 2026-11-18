# 🌽 Terminal de Vendas para Agricultura Familiar (PDV)

**Projeto 04** – Sistema interativo em Python que simula um caixa de feira livre, pensado para pequenos produtores comercializarem produtos como macaxeira, feijão de corda, queijo coalho e rapadura, calculando totais e troco.

---

## 📋 Funcionalidades

- **Abertura de Caixa:** o sistema carrega um catálogo de produtos disponíveis com seus preços.
- **Adição ao Carrinho:** o usuário digita o nome do produto e a quantidade; o sistema calcula o subtotal e adiciona o item ao carrinho.
- **Checkout e Troco:** o sistema soma tudo, pede o valor pago em dinheiro e calcula o troco, alertando caso o valor seja insuficiente.

## 🧱 Estrutura de Código

- **Dicionários:** um dicionário para o catálogo (chave: nome do produto, valor: preço) e outro para o carrinho de compras.
- **Laços de repetição:** um laço `while` mantém a adição de itens ativa até o usuário digitar `Finalizar`.
- **I/O formatado:** valores monetários exibidos com f-strings formatadas (ex.: `f"R$ {valor:.2f}"`).

## ▶️ Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```
2. Execute o programa:
   ```bash
   python main.py
   ```
   > Troque `main.py` pelo nome do seu arquivo, se for diferente.

## 💡 Exemplo de uso

```
=== PDV - Feira da Agricultura Familiar ===
Produtos disponíveis:
- Macaxeira: R$ x.xx
- Feijão de corda: R$ x.xx
- Queijo coalho: R$ x.xx
- Rapadura: R$ x.xx

Produto (ou 'Finalizar'): Macaxeira
Quantidade: 2
Adicionado! Subtotal: R$ x.xx

Produto (ou 'Finalizar'): Finalizar

Total da compra: R$ x.xx
Valor pago: R$ 50.00
Troco: R$ x.xx
```

> Ajuste os valores e o texto acima de acordo com o seu programa.

## 🛠️ Tecnologias

- Python 3

## 👤 Autor

**Desenvolvido por** – Eduardo Moraes, Antonio Salatiel e Amanda Vieira 
Curso: Sistema de Informação /Disciplina: IP-Introdução a Programação  
UAST-UFRPE, 2026
