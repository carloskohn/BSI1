#!/bin/env python3
# Marco André Mendes <marco.mendes@ifc.edu.br>
# Criada por Felipe Tiago Guimarães <felipeguimaraes0025@gmail.com>
# Exercícios retirados do livro de Python de Raul Waslawick
# Lista de exercícios 2 - while


def fatorial(numero):
    ''' Calcule e retorne o fatorial do 'numero' informado,
    O fatorial é o valor produtório dos valores menores ou iguais ao número
    ex: fatorial de 4 é 4*3*2*1 e retorna 24'''

    contador = 1
    fat = 1

    while contador <= numero:
        fat *= contador
        contador += 1

    return fat


def corrida(vantagem, vlc_tartaruga, vlc_lebre):
    """A tartaruga e a lebre vão apostar uma corrida. A lebre concede à
        tartaruga o direito de sair a uma vantagem em metros a sua frente.
        A tartarua corre a uma velocidade em metros por segundo (vlc_tartaruga)
        e a lebre corre a uma outra velocidade em metros por segundo (vlc_lebre).
        Desenvolva uma função que calcule quantos minutos são necessários para
        a lebre alcançar a tartaruga."""

    segundos = 0
    dist_percorrida_lebre = 0

    if vantagem == 0:
        return vantagem
    if vantagem > 0 and vlc_tartaruga > vlc_lebre:
        return -1
    else:
        while dist_percorrida_lebre <= vantagem:
            dist_percorrida_lebre += vlc_lebre
            vantagem += vlc_tartaruga
            segundos += 1

    return segundos



def sub_sucessivas(dividendo, divisor):
    """Escreva um programa que calcula a divisão inteira e o resto da divisão inteira
    entre dois números inteiros positivos usando o método das subtrações sucessivas.
    A técnica consiste em subtrair o divisor do dividendo até que o dividendo se torne
    menor que o divisor. Neste instante, o número de subtrações feitas será o valor da
    divisão inteira e o valor atual do dividendo será o resto.
    Não vale roubar usando módulos prontos do Python e obviamente divisão por
    ZERO não é permitida, afinal não conseguimos representar o INFINITO =)"""

    contador = 0

    if divisor == 0:
        return "Parabéns, vc alcançou o Infinito!!"
    else:
        while dividendo >= divisor:
            dividendo -= divisor
            contador += 1

    return (contador, dividendo)


def compra(aplicacao, valor_carro):
    """Você tem uma certa aplicação financeira com um saldo determinado, que
    rende 0.7% ao mês. Você deseja comprar um carro que custa um determinado
    preço. Porém, o preço do carro sobe à uma taxa de 0,4% ao mês.
    Faça um programa que calcule quantos meses serão necessários até que,
    com essa aplicação, você consiga comprar o carro à vista."""

    cont_meses = 0

    if aplicacao >= valor_carro:
        return 0
    else:
        while aplicacao < valor_carro:
            aplicacao += aplicacao * 0.007
            valor_carro += valor_carro * 0.003
            cont_meses += 1

        return cont_meses


def serie_infinita(x, i):
    """Faça um programa que tenha como objetivo se aproximar da série
     infinita e^x.
     A fórmula de aproximação é a seguinte:
        e^x = 1 + x + (x²/2!) + (x³/3!) + (x⁴/4!) + ...
    Sendo i o número de termos somados. Quanto maior o número de termos,
    maior a precisão do valor encontrado.
    Na expressão, cada uma das partes formadas por (x^y/y!) é denominada termo."""

    soma = 1 + x
    contador = 1
    y = 2

    if i == 0:
        return x
    else:
        while contador < i:
            termo = x ** y / fatorial(y)
            contador += 1
            y += 1
            soma += termo

    return soma


def populacao_dodo(populacao):
    """ O dodô é uma ave não voadora, extinta atualmente, e que era endêmica
    da ilha Mauritius, na costa leste da África. A população inicial de dodôs
    era de 1 milhão de indivíduos no ínicios de 1600. A partir dessa data, durante
    cada ano, 6% dos animais vivos do começo do ano morreram. O número de animais
    nascidos ao longo do ano foi de 1% da população anual.
    Escreva um programa que retorne o ano em que a população de dodôs cai para
    menos de 10% da população inicial."""

    ano = 1600
    nascimentos = 0
    mortes = 0
    dez_porcento = populacao / 10

    while populacao >= dez_porcento:
        nascimentos = populacao * 0.01
        mortes = populacao * 0.06
        populacao = populacao - mortes + nascimentos
        ano += 1

    return ano


def matriz(n):
    """Crie uma matriz quadrada nxn utilizado while, cuja função de
    atribuição é A[i][j] = i+j. A partir da matriz criada, retorne a
    soma da diagonal principal."""

    soma = 0
    contador = 1
    i = 0
    j = 0

    while contador <= n:
        i += 1
        j += 1
        contador +=1
        soma += i + j
    return soma


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31mFalhou'
    else:
        prefixo = '\033[32mPassou'
        acertos += 1
    print('{} Esperado: {} \tObtido: {}\033[1;m'.format(
        prefixo, esperado, obtido))


def main():

    print('Fatorial:')
    test(fatorial(0), 1)
    test(fatorial(1), 1)
    test(fatorial(5), 120)
    test(fatorial(10), 3628800)


    print('Corrida:')
    test(corrida(100, 2, 5), 34)
    test(corrida(200, 7, 6), -1)
    test(corrida(0, 2, 5), 0)
    test(corrida(0, 7, 6), 0)
    test(corrida(5884, 4, 5), 5885)

    print('Suntrações Sucessivas:')
    test(sub_sucessivas(17, 4), (4, 1))
    test(sub_sucessivas(50, 5), (10, 0))
    test(sub_sucessivas(3, 9), (0, 3))
    test(sub_sucessivas(25, 1), (25, 0))
    test(sub_sucessivas(24, 0), ("Parabéns, vc alcançou o Infinito!!"))

    print('Compra:')
    test(compra(10000.00, 12000.00), (46))
    test(compra(15000.00, 22000.00), (97))
    test(compra(40000.00, 32000.00), (0))
    test(compra(50000.00, 52000.00), (10))

    print('Série Infinita:')
    test(serie_infinita(2, 2), (5.0))
    test(serie_infinita(1, 0), (1.0))
    test(serie_infinita(2, 7), (7.3809523809523805))
    test(serie_infinita(2, 6), (7.355555555555555))
    test(serie_infinita(2, 1), (3.0))
    test(serie_infinita(7, 57), (1096.6331584284578))

    print('População Dodo:')
    test(populacao_dodo(1000000), 1645)

    print('Matriz:')
    test(matriz(4), 20)
    test(matriz(2), 6)
    test(matriz(7), 56)
    test(matriz(5), 30)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
