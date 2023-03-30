Nome : str = input('Olá, qual seu nome? ')
Idadeatual : int = int(input('Qual sua idade atual? '))
Anoatual : int = int(input('Qual o ano atual? '))
Anofuturo : int = int(input("Em que ano quer simular sua idade? "))

Diferença : int = Anofuturo - Anoatual
Idadefutura : int = Idadeatual + Diferença

print("\n{} no ano de {} você terá {} anos".format(Nome, Anofuturo, Idadefutura))