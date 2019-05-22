def multa_excesso_velocidade (velocidade):
    """Receba a velocidade de um carro, supondo um valor inteiro.
       Caso ultrapasse 110Km/h exiba uma mensagem dizendo que o usuário foi multado.
       Neste caso, exiba o valor da multa, cobrando R$5,00 por km acima de 110"""

    if velocidade <= 110:
        return 0
    if velocidade > 110:
        return (velocidade - 110) * 5


print(multa_excesso_velocidade(109)) #0
print(multa_excesso_velocidade(110)) #0
print(multa_excesso_velocidade(111)) #5
print(multa_excesso_velocidade(120)) #50


def conta_telefone (minutos):
    """Até 200 min. R$ 0,20, até 400 min. R$ 0,18 e acima 400min R$ 0,15"""
    if minutos <= 200:
        valor_conta = minutos * 0.2
    elif minutos <= 400:
        valor_conta = minutos * 0.18
    else:
        valor_conta = minutos * 0.15

    return round(valor_conta,2)


print(conta_telefone(199)) #39.8
print(conta_telefone(200)) #40
print(conta_telefone(201)) #36.18
print(conta_telefone(399)) #71.82
print(conta_telefone(400)) #72
print(conta_telefone(401)) #60.15


def Quebra_dada (data):
    """quebre a data em dia, mês e ano"""

    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    return dia, mes, ano

print(Quebra_dada("22/12/1978")) #22, 12, 1978


