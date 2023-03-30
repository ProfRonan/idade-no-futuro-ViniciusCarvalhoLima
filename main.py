Nome : str = input('Olá, qual seu nome? ')
idade_str = input('Qual sua idade atual? ')
if idade_str.isnumeric():
    Idadeatual = int(idade_str)
Anoatual_str = input('Qual o ano atual? ')
if Anoatual_str.isnumeric():
    Anoatual = int(Anoatual_str)
Anofuturo_str = input("Em que ano quer simular sua idade? ")
if Anofuturo_str.isnumeric():
    Anofuturo = int(Anofuturo_str)

Diferença : int = Anofuturo - Anoatual
Idadefutura : int = Idadeatual + Diferença

print("\n{} no ano de {} você terá {} anos".format(Nome, Anofuturo, Idadefutura))