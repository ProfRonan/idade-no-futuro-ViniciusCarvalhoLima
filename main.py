Nome = input('Olá, qual seu nome? ')
Anoatual = int(input('Qual o ano atual? '))
Idadeatual = int(input('Qual sua idade atual? '))
Anofuturo = int(input('Em que ano quer simular sua idade? '))

Diferença : int = Anofuturo - Anoatual
Idadefutura : int = Idadeatual + Diferença

print("\n{}, no ano de {} você terá {} anos".format(Nome, Anofuturo, Idadefutura))