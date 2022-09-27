# 26º Estrutura de Funções
# Uma função é um bloco de código que só é executado quando é chamado.
#
# Você pode passar dados, conhecidos como parâmetros, para uma função.
#
# Uma função pode retornar dados como resultado.

# Funções simples
def Somar(Valor1, Valor2):
  Soma = Valor1 + Valor2
  print(Soma)

Somar(-67.900, 10.121233)

def Boas_Vindas():
  print('********* PYTHON **************')

Boas_Vindas()

from random import randint
# Função
def Sobrenome( Algum_Texto, Numero ):
  print(f'Nome dele é: {Algum_Texto}')

  if Numero >= 10:
    print('Maior que 10')
  else:
    print('NADA!')

Lista_Nomes = ['Odemir', 'Luigi', 'Mariana']

for Nome in Lista_Nomes:
  Sobrenome( Nome, randint(1,12) )