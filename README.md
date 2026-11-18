# 🌽 Terminal de Vendas para Agricultura Familiar (PDV)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-2e7d32)
![Projeto](https://img.shields.io/badge/Projeto-04-c0502a)

Sistema interativo em **Python** que simula um **caixa de feira livre**, ideal para pequenos produtores da agricultura familiar comercializarem produtos como **macaxeira, feijão de corda, queijo coalho e rapadura**, calculando totais e troco de forma simples e rápida.

> Projeto desenvolvido para a disciplina de **Introdução à Programação (IP)** – UAST/UFRPE.

---

## 📑 Sumário

- [Funcionalidades](#-funcionalidades)
- [Como funciona](#-como-funciona)
- [Estrutura de código](#-estrutura-de-código)
- [Como executar](#️-como-executar)
- [Exemplo de uso](#-exemplo-de-uso)
- [Tratamento de erros](#️-tratamento-de-erros)
- [Possíveis melhorias](#-possíveis-melhorias)
- [Tecnologias](#️-tecnologias)
- [Autores](#-autores)

---

## 📋 Funcionalidades

- **Abertura de Caixa:** o sistema carrega um catálogo de produtos disponíveis com seus respectivos preços.
- **Adição ao Carrinho:** o usuário digita o nome do produto e a quantidade; o sistema calcula o subtotal e adiciona o item ao carrinho.
- **Checkout e Troco:** o sistema soma tudo, pede o valor pago em dinheiro e calcula o troco, alertando caso o valor seja insuficiente.

## 🔄 Como funciona

```
Abrir caixa (carrega catálogo)
        │
        ▼
┌─► Digitar produto ──► "Finalizar"? ──► Sim ──► Checkout
│        │                                         │
│        ▼ Não                                     ▼
│   Digitar quantidade                      Somar total
│        │                                         │
│        ▼                                         ▼
│   Calcular subtotal                       Pedir valor pago
│        │                                         │
│        ▼                                         ▼
└── Adicionar ao carrinho                   Valor suficiente? ─► Calcular troco
                                                   │
                                                   ▼ Não
                                             Alertar e pedir novamente
```

## 🧱 Estrutura de código

| Conceito | Como foi aplicado |
|---|---|
| **Dicionários** | Um para o catálogo (`chave: nome do produto`, `valor: preço`) e outro para o carrinho de compras. |
| **Laços de repetição** | Um laço `while` mantém a adição de itens ativa até o usuário digitar `Finalizar`. |
| **I/O formatado** | Valores monetários exibidos com f-strings, ex.: `f"R$ {valor:.2f}"`. |

## ▶️ Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>

# 2. Entre na pasta do projeto
cd <nome-da-pasta>

# 3. Execute o programa
python main.py
```

> 💡 Troque `main.py` pelo nome real do seu arquivo, se for diferente.

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

> Substitua os valores acima pela saída real do seu programa.

## ⚠️ Tratamento de erros

- **Produto inexistente:** o sistema avisa que o item não está no catálogo e pede novamente.
- **Valor pago insuficiente:** o sistema alerta e informa quanto ainda falta.

## 🚀 Possíveis melhorias

- Remover itens do carrinho antes de finalizar.
- Salvar o histórico de vendas em arquivo.
- Controle de estoque dos produtos.
- Cadastro de novos produtos pelo próprio produtor.

## 🛠️ Tecnologias

- Python 3

## 👥 Autores

| Nome |
|---|
| Eduardo Moraes |
| Antonio Salatiel |
| Amanda Vieira |
| Thyago Silva|

**Curso:** Sistemas de Informação  
**Disciplina:** IP – Introdução à Programação  
**Instituição:** UAST – UFRPE, 2026
