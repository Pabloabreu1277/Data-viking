# 28º Estrutura TRY
# O try permite testar um bloco de código quanto a erros.
#
# O except permite que você lide com o erro.
#
# O else permite executar código quando não há erro.
#
# O finally permite que você execute código, independentemente do resultado dos blocos try e except.
#
# #

try:
  0 / 0
except:
  print('Deu Ruim!!!')

try:
  print(Algo_Coisa_Que_Nao_Defini)

except NameError:
  print("Ops deu algum erro!")

finally:
  print("Vou ser executado de qualquer forma")