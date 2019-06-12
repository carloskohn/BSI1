#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 8a - revisão

def dormir(dia_semana, feriado):
    """
    dia_semana é True para dias na semana
    feriado é True nos feriados
    você pode ficar dormindo quando é feriado ou não é dia semana
    retorne True ou False conforme você vá dormir ou não
    """
    # if feriado or not dia_semana:
    #     return True
    # else:
    #     return False

    return feriado or not dia_semana


def alunos_problema(a_sorri, b_sorri):
    """
    temos dois alunos a e b
    a_sorri e b_sorri indicam se a e b sorriem
    temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
    retorne True quando houver problemas
    """
    return a_sorri == b_sorri

def soma_dobro(a, b):
    """
    dados dois números inteiros retorna sua soma
    porém se os números forem iguais retorna o dobro da soma
    soma_dobro(1, 2) -> 3
    soma_dobro(2, 2) -> 8
    """
    if a == b:
        soma = (a + b) * 2
    else:
        soma = a + b

    return soma


def diff21(n):
    """
    dado um inteiro n retorna a diferença absoluta entre n e 21
    porém se o número for maior que 21 retorna o dobro da diferença absoluta
    diff21(19) -> 2
    diff21(25) -> 8
    dica: abs(x) retorna o valor absoluto de x
    """
    if n <= 21:
        soma = 21 - n
    else:
        soma = (n - 21) * 2

    return soma


def papagaio(falando, hora):
    """
    temos um papagaio que fala alto
    hora é um parâmetro entre 0 e 23
    temos problemas se o papagaio estiver falando antes da 7 ou depois das 20
    """

    return falando and ((hora < 7) or (hora > 20))

    # if not falando:
    #     return False
    # elif hora < 7 or hora > 20:
    #     return True
    # else:
    #     return False


def dez(a, b):
    """
    dados dois inteiros a e b
    retorna True se um dos dois é 10 ou a soma é 10
    """

def dista10(n):
    """
    seja um inteiro n
    retorna True se a diferença absoluta entre n e 100 ou n e 200
    for menor ou igual a 10
    dista10(93) -> True
    dista10(90) -> True
    dista10(89) -> False
    """

def apaga(s, n):
    """
    seja uma string s e um inteiro n
    retorna uma nova string sem a posição n
    apaga('kitten', 1) -> 'ktten'
    apaga('kitten', 4) -> 'kittn'
    """

def troca(s):
    """
    seja uma string s
    se s tiver tamanho <= 1 retorna ela mesma
    caso contrário troca a primeira e última letra
    troca('code') -> 'eodc'
    troca('a') -> 'a'
    troca('ab') -> 'ba'
    """

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' %('Falhou')
    else:
        prefixo = '\033[32m%s' %('Passou')
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():
  print ('Oba! Hoje vou ficar dormindo!')
  test(dormir(False, False), True)
  test(dormir(True, False), False)
  test(dormir(False, True), True)
  test(dormir(True, True), True)

  print ()
  print ('Alunos problema')
  test(alunos_problema(True, True), True)
  test(alunos_problema(False, False), True)
  test(alunos_problema(True, False), False)
  test(alunos_problema(False, True), False)

  print ()
  print ('Soma dobro')
  test(soma_dobro(1, 2), 3)
  test(soma_dobro(3, 2), 5)
  test(soma_dobro(2, 2), 8)
  test(soma_dobro(-1, 0), -1)
  test(soma_dobro(0, 0), 0)
  test(soma_dobro(0, 1), 1)

  print ()
  print ('Diff21')
  test(diff21(19), 2)
  test(diff21(10), 11)
  test(diff21(21), 0)
  test(diff21(22), 2)
  test(diff21(25), 8)
  test(diff21(30), 18)

  print ()
  print ('Papagaio')
  test(papagaio(True, 6), True)
  test(papagaio(True, 7), False)
  test(papagaio(False, 6), False)
  test(papagaio(True, 21), True)
  test(papagaio(False, 21), False)
  test(papagaio(True, 23), True)
  test(papagaio(True, 20), False)

  print ()
  print ('Dez')
  test(dez(9, 10), True)
  test(dez(9, 9), False)
  test(dez(1, 9), True)
  test(dez(10, 1), True)
  test(dez(10, 10), True)
  test(dez(8, 2), True)
  test(dez(8, 3), False)
  test(dez(10, 42), True)
  test(dez(12, -2), True)

  print ()
  print ('Dista 10')
  test(dista10(93), True)
  test(dista10(90), True)
  test(dista10(89), False)
  test(dista10(110), True)
  test(dista10(111), False)
  test(dista10(121), False)
  test(dista10(0), False)
  test(dista10(5), False)
  test(dista10(191), True)
  test(dista10(189), False)
  test(dista10(190), True)
  test(dista10(200), True)
  test(dista10(210), True)
  test(dista10(211), False)
  test(dista10(290), False)

  print ()
  print ('Apaga')
  test(apaga('kitten', 1), 'ktten')
  test(apaga('kitten', 0), 'itten') 
  test(apaga('kitten', 2), 'kiten') 
  test(apaga('kitten', 4), 'kittn')
  test(apaga('Hi', 0), 'i')
  test(apaga('Hi', 1), 'H')
  test(apaga('code', 0), 'ode')
  test(apaga('code', 1), 'cde')
  test(apaga('code', 2), 'coe')
  test(apaga('code', 3), 'cod')
  test(apaga('chocolate', 8), 'chocolat')

  print ()
  print ('Troca letras')
  test(troca('code'), 'eodc')	    
  test(troca('a'), 'a')
  test(troca('ab'), 'ba')
  test(troca('abc'), 'cba')
  test(troca(''), '')
  test(troca('Chocolate'), 'ehocolatC')
  test(troca('nythoP'), 'Python')
  test(troca('hello'), 'oellh')



if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
