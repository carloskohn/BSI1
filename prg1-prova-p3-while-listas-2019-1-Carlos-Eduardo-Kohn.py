#!/bin/env python3
# Marco André <marco.mendes@ifc.edu.br>
# Avaliação - Faça os exercícios utilizando repetição com while
# Renomeie o arquivo, incluindo seu nome.
# Coloque o nome do arquivo como assunto do email e envie para o
# endereço acima.


def quantidade_de_pares(valor_inicial, valor_final):
    ''' Determine a quantidade de números ímpares num intervalo.
    Dica: inclua os extremos, isso é, o valor_inicial e o valor final do
    intervalo.'''

    quant_pares = 0


    while valor_inicial <= valor_final:
        if valor_inicial %2 == 0:
            quant_pares += 1
        valor_inicial += 1

    return quant_pares


def Fibonacci(n):
    ''' Retorne uma lista com os primeiros "n" elementos da série de Fibonacci
    Fibonacci = 1,1,2,3,5,8,13,...'''

    contador = 1
    numero_atual = 1
    proximo_numero = 0
    numero_anterior = 0
    lista = [1, ]


    while contador < n:
        proximo_numero = numero_atual + numero_anterior
        numero_anterior = numero_atual
        numero_atual = proximo_numero
        contador += 1
        lista.append(numero_atual)

    return lista



def serie_pi(vezes):
    ''' Calcule o valor de pi através da série
    4/1 - 4/3 + 4/5 - 4/7 + ... - 4/n, sendo informado o número de
    itens (vezes).'''

    contador = 1
    m = 1
    soma = 0

    while contador <= vezes:
        if contador % 2 != 0:
            soma += 4 / m
            contador += 1
            m += 2
        else:
            soma -= 4 / m
            contador += 1
            m += 2

    return round(soma, 6)


def intercalamento_contrario(lista1, lista2):
    ''' Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo intercalamento entre as duas.
    A primeira lista deve ser usada na ordem normal. Já a segunda, deve
    ser utilizada na ordem inversa.'''

    nova_lista = []
    posiçao_lista1 = 0
    posiçao_lista2 = -1

    for numero in lista1:
        nova_lista.append(lista1[posiçao_lista1])
        nova_lista.append(lista2[posiçao_lista2])
        posiçao_lista1 += 1
        posiçao_lista2 += -1

    return nova_lista


def maiores_13(idades, alturas):
    '''Esta função recebe as idades e alturas de diversas pessoas, em duas
    listas separadas e de igual comprimento.
    Calcule a media das alturas e retorne as alturas daqueles que possuem
    'idades' maior que 13 e altura inferior a media de altura da turma'''

    altura_total = 0
    maior13_inferiormedia = []

    for altura in alturas:
        altura_total += altura
    media_alturas = altura_total / len(alturas)

    for posicao, idade in enumerate(idades):
        if idade > 13 and alturas[posicao] < media_alturas:
            maior13_inferiormedia.append(alturas[posicao])

    return maior13_inferiormedia


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Quantidade de pares:')
    test(quantidade_de_pares(1, 1), 0)
    test(quantidade_de_pares(1, 2), 1)
    test(quantidade_de_pares(2, 3), 1)
    test(quantidade_de_pares(2, 4), 2)
    test(quantidade_de_pares(1, 10), 5)

    print('Fibonnaci:')
    test(Fibonacci(1), [1])
    test(Fibonacci(2), [1, 1])
    test(Fibonacci(3), [1, 1, 2])
    test(Fibonacci(4), [1, 1, 2, 3])
    test(Fibonacci(5), [1, 1, 2, 3, 5])

    print('Série pi:')
    test(serie_pi(1), 4.000000)
    test(serie_pi(2), 2.666667)
    test(serie_pi(3), 3.466667)
    test(serie_pi(4), 2.895238)
    test(serie_pi(5), 3.339683)
    test(serie_pi(6), 2.976046)
    test(serie_pi(7), 3.283738)
    test(serie_pi(8), 3.017072)
    test(serie_pi(1000), 3.140593)
    test(serie_pi(9000), 3.141482)

    print(' Lista intercalada contrária:')
    test(intercalamento_contrario([], []), [])
    test(intercalamento_contrario([1], [2]), [1, 2])
    test(intercalamento_contrario([1, 2], [3, 4]), [1, 4, 2, 3])
    test(intercalamento_contrario([1, 2, 3], [4, 5, 6]), [1, 6, 2, 5, 3, 4])
    test(intercalamento_contrario([1, 2, 3, 4, 5], [
         6, 7, 8, 9, 10]), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6])

    print(' Alturas abaixo da media:')
    test(maiores_13([13, 13, 14], [1.7, 1.7, 1.5]), [1.5])
    test(maiores_13([13, 13, 14, 13], [1.7, 1.7, 1.5, 1.6]), [1.5])
    test(maiores_13([14, 20], [1.6, 2]), [1.6])
    test(maiores_13([10, 7, 13, 15, 20, 21], [
         1.7, 1.21, 1.65, 2, 1.9, 1.5]), [1.5])
    test(maiores_13([14, 15, 16, 17, 18, 30], [
         1.9, 1.89, 1.85, 1.95, 2, 1.99]), [1.9, 1.89, 1.85])
    test(maiores_13([10, 9, 90, 9, 13, 14, 15], [
         1.25, 1.3, 1.7, 1.41, 1.5, 1.55, 1.7]), [])


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")