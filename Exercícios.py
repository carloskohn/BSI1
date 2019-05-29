# math - módulo matemático
# Ex: import math
#
# split - quebra uma string no ponto escolhido
# Ex: variável de hora ou data - variável.split(“o ponto onde se quer quebrar”)
# Recebe um horário no formato 24 horas e retorna no formato am/pm
#  am: antes do meio-dia
#  pm: depois do meio-dia
#
#  hora, minuto = horario.split(":")
#
#  if int(hora) < 13:
#      return (str(hora)+":"+minuto+ " am")
#  else:
#      return (str(int(hora)-12) + ":" +minuto + " pm")
#
# Outra maneira de quebrar data:
# data = "22/12/1978"
# dia = int(data[:2])
# mes = int(data[3:5])
# ano = int(data[6:])
#
# print (dia, mes, ano)
#
# upper - devolve tudo em maiúsculo
# Ex: a = ‘Carlos’
# print(a.upper())
# CARLOS
#
# lower - devolve tudo em minúsculo
# Ex: a = ‘Carlos’
# print(a.lower())
# carlos
#
# title - devolve a primeira letra de cada palavra em maiúsculo
# Ex: variavel.title()
#
# strip - remove os espaços da variavel
# Ex: variavel.strip()
#
#
# capitalize - devolve a primeira letra da frase em maiúscula
# Ex: variavel.capitalize()
#
# input - Pede que o usuário insira algum dado
# Ex: input (‘Insira um dado: ’)
#
# len - retorna a quantidade de caracteres de uma variável
# Ex: len (variavel)
#
# round - arredonda o valor depois do número inteiro na quantidade de casas que queira
# Ex: round (variável, ?) nesse caso, o ponto de interrogação deve ser substituído por um nº
#
# sqrt - calculo de raiz
# Ex: math.squt(9) Resultado=3
#
# ceil - arredonda para cima
# Ex: math.ceil(5/2) Resultado=3
#
# floor - arredonda para baixo
# Ex: math.floor(5/2) Resultado=2
#
# append - retorna algo se houver, deve ser criado uma variável vazia com chaves
# Ex: lista = [ ]
# lista.append()
#
#
#
#
# \n - “Barra invertida+n” recurso usado para pular a linha
# Ex: print('Carlos \nEduardo\nKohn')
# Carlos
# Eduardo
# Kohn
#
#
#
# dia = input ('Dia: ')
# mes = input ('Mês: ')
# ano = input ('Ano: ')
# print ('Você nasceu no dia ', dia, 'de ', mes, 'de ', ano, '. Correto?')
#
#
# salario = float (input("Salário Atual: R$"))
# percentual_de_aumento = float (input('Percentual de Aumento: '))
# salario_final = salario * (percentual_de_aumento / 100) + salario
# print ("Salário Atualizado: R$ %.2f" % salario_final)
#
#
# variavel1 = 2
# variavel2 = 3
# variavel3 = 4
# print(variavel1 + variavel2 + variavel3)
#
#
#    soma_valores = a + b + c
#    return soma_valores
#
# print(soma(10,10,10))
# print(soma("Carlos ","Eduardo ","Kohn"))
#
#
#
# novo_salario = salario + (salario * porcentagem/100)
# return round (novo_salario, 2)
# def multa_excesso_velocidade (velocidade):
#    """Receba a velocidade de um carro, supondo um valor inteiro.
#       Caso ultrapasse 110Km/h exiba uma mensagem dizendo que o usuário foi multado.
#       Neste caso, exiba o valor da multa, cobrando R$5,00 por km acima de 110"""
#
#    if velocidade <= 110:
#        return 0
#    if velocidade > 110:
#        return (velocidade - 110) * 5
#
# print(multa_excesso_velocidade(109)) #0
# print(multa_excesso_velocidade(110)) #0
# print(multa_excesso_velocidade(111)) #5
# print(multa_excesso_velocidade(120)) #50
#
#
# def conta_telefone (minutos):
#    """Até 200 min. R$ 0,20, até 400 min. R$ 0,18 e acima 400min R$ 0,15"""
#    if minutos <= 200:
#        valor_conta = minutos * 0.2
#    elif minutos <= 400:
#        valor_conta = minutos * 0.18
#    else:
#        valor_conta = minutos * 0.15
#
#    return round(valor_conta,2)
#
# print(conta_telefone(199)) #39.8
# print(conta_telefone(200)) #40
# print(conta_telefone(201)) #36.18
# print(conta_telefone(399)) #71.82
# print(conta_telefone(400)) #72
# print(conta_telefone(401)) #60.15
#
#
#
#
#
#
#
#
#
# def data_valida(data):
#    """Valida data. Recebe uma string no formato dd/mm/aaaa e informa
#    um valor lógico indicando se a data é válida ou não."""
#
#    dia = int(data[:2])
#    mes = int(data[3:5])
#    ano = int(data[6:])
#    mes_30 = [4, 6, 9, 11]
#    mes_31 = [1, 3, 5, 7, 8, 10, 12]
#    ultimo_dia_mes
#    if ano>=1 and mes>=1 and mes<=12 and dia>=1 and dia <= ultimo_dia_mes:
#        return True
#    else:
#        return False
#
#
#
# variavel = variavel.strip().lower()
# novo_variavel = ‘ ’
# for caracter in variavel:
# 	if caracter.isalnum():
# 		novo_variavel += caracter
#
# return novo_variavel == novo_variavel[::-1]
