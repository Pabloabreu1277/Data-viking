# 24º Estrutura de Loop WHILE
# Python While Loop é usado para executar um bloco de instruções repetidamente até que uma determinada condição seja satisfeita. E quando a condição se torna falsa, a linha imediatamente após o loop no programa é executada. While loop se enquadra na categoria de iteração indefinida . A iteração indefinida significa que o número de vezes que o loop é executado não é especificado explicitamente com antecedência.

while expressão:

loop
# While
Loop = 0

while Loop <= 10:
  print( Loop )
  Loop += 1

# While
Loop = 0

while Loop <= 10:
    print(Loop)
    Loop += 1

    if Loop == 5:

        for c in range(10):
            print(c)
# While True
# Joginho
import random

while True:

  Jogador1 = random.randint(0, 6)
  Jogador2 = random.randint(5, 10)

  if Jogador1 > Jogador2:
    print(Jogador1, '-', Jogador2, 'FINALMENTE !!!!!!!!!!!')
    break

  else:
    print(Jogador1, '-', Jogador2)