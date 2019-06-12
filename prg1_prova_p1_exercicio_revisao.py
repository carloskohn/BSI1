#!/bin/env python3
# coding: utf-8

# Marco André <marcoandre@gmail.com>
# Exercícios de revisão P1


def calcula_aumento_salario1(salario):
    """Calcula aumento do salário, de acordo com a seguinte tabela:
        Salário até 280: aumento de 20%
        Salário até 700: aumento de 15%
        Salário até 1500: aumento de 10%
        Salário acima de 1500: aumento de 5%
     """

    if salario <= 280:
        aumento = salario * 0.2
        novo_salario = salario + aumento
        return (salario, 20, aumento, novo_salario)
    if salario > 280 and salario <= 700:
        aumento = salario * 0.15
        novo_salario = salario + aumento
        return (salario, 15, aumento, novo_salario)
    if salario > 700 and salario <= 1500:
        aumento = salario * 0.1
        novo_salario = salario + aumento
        return (salario, 10, aumento, novo_salario)
    else:
        aumento = salario * 0.05
        novo_salario = salario + aumento
        return (salario, 5, aumento, novo_salario)


def calcula_idade(ano_nascimento, ano_atual):
    """Calcula idade."""

    idade = ano_atual - ano_nascimento
    return idade
    

def calcula_media(prova, trabalho, exercicio):
    """ Calcula media:
    Prova com peso 7
    Trabalho com peso 2
    Exercício com peso 1
    """
    media = (prova * .7) + (trabalho * .2) + (exercicio * .1)
    return media


def calcula_idade_canina(idade_humana, porte_do_cao):
    '''Calcule sua idade canina:
    - cães de porte pequeno: dividir sua idade por 5
    - cães de porte médio: dividir sua idade por 6 
    - cães grandes: dividir sua idade por 7'''

    if porte_do_cao == "pequeno":
        idade_canina = idade_humana // 5
        return (idade_canina)
    if porte_do_cao == "medio":
        idade_canina = idade_humana // 6
        return (idade_canina)
    else:
        idade_canina = idade_humana // 7
        return (idade_canina)


def calcula_aumento_salario(salario_atual):
    ''' Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5% 
    Salário mínimo para referência: R$ 724,00
    '''

    s_m = 724

    if salario_atual <= s_m:
        novo_salario = salario_atual * 1.2
        return round(novo_salario, 2)
    if salario_atual > s_m and salario_atual <= s_m * 2:
        novo_salario = salario_atual * 1.15
        return round(novo_salario, 2)
    if salario_atual > s_m * 2 and salario_atual <= s_m * 5:
        novo_salario = salario_atual * 1.1
        return round(novo_salario, 2)
    else:
        novo_salario = salario_atual * 1.05
        return round(novo_salario, 2)


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' %'Falhou'
    else:
        prefixo = '\033[32m%s' %'Passou'
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():
    print('Calcula aumento salário:')
    test(calcula_aumento_salario1(100),(100, 20, 20.0, 120.0))
    test(calcula_aumento_salario1(1500),(1500, 10, 150.0, 1650.0))
    test(calcula_aumento_salario1(3000),(3000, 5, 150.0, 3150.0))

    print('Calcula idade:')
    test(calcula_idade(1973,2015),42)
    test(calcula_idade(2000,2015),15)
    test(calcula_idade(2015,2015),0)

    print('Idade canina:')
    test(calcula_idade_canina(40,'pequeno'),8)
    test(calcula_idade_canina(40,'medio'),6)
    test(calcula_idade_canina(40,'grande'),5)

    print('Calcula média:')
    test(calcula_media(10, 10, 10),10) 
    test(calcula_media(7, 7, 7),7) 
    test(calcula_media(5, 8, 10),6.1) 

    print('Aumento salarial:')
    # até 1 SM: 20%
    test(calcula_aumento_salario(500.00), 600.00) 
    test(calcula_aumento_salario(724.00), 868.80) 
    # 1-2 SM: 15%
    test(calcula_aumento_salario(725.00), 833.75)
    test(calcula_aumento_salario(1448.00), 1665.20)
    # 2-5 SM: 10%
    test(calcula_aumento_salario(1449.00), 1593.90)
    test(calcula_aumento_salario(3620.00), 3982.00)
    # >5 SM: 5%
    test(calcula_aumento_salario(3621.00), 3802.05)
    test(calcula_aumento_salario(4000.00), 4200.00)

     
if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
