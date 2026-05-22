# Versionamento


## Objetivo da atividade: Função PYTHON para calcular porcentagem

###### autor e e-mail: Justino - arturskateeveryday@gmail.com
###### disciplina: versionamento
###### data: 22/05/2026



### funcionalidades implementadas:

1. Método para cálculo porcentagens da lista de valores [(valor, percentual)]
2. Método que efetua o acréscimo de valor conforme a lista enviada [(valor, percentual)]
3. Método para redução de valor conforme a lista enviada [(valor, percentual)]

### funções criadas:
1. calculate_percentage([(valor, percentual)])
2. add_percentage([(valor, percentual)])
2. reduce_percentage([(valor, percentual)])


### breve explicação dos cálculos desenvolvidos:
1. Para calcular porcentagem:
        valor * valor divido por cem (100)
2. Para fazer um aumento de valor:
        valor + (valor * valor divido por cem (100))
3. Para fazer o desconto:
        valor -(valor * valor divido por cem (100))


### instruções básicas de uso do notebook
Para utilização deste notebook, basta efetuar o get e compilar com Python 3+:
As funções recebem a lista do carrinho contendo (valor, percentual)

```
    shop_cart = [(500, 10), (800, 25), (260, 38)]
    add_percentage(shop_cart)
```