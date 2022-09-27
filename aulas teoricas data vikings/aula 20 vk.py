# 20° Pacote
# Externo - Random
# Este
# módulo
# implementa
# geradores
# de
# números
# pseudo - aleatórios
# para
# várias
# distribuições.

# import random
import random

# Lista numerico
Lista_Numerica = [1, 2, 3, 4, 5, 6]
print(f'O número sorteado foi: {random.choice(Lista_Numerica)} \n')

# Sortear uma letra da palavra
Palavra = 'Odemir'
print(f'A Letra sorteada foi: {random.choice(Palavra)} \n')

# Numero aleatorio entre 0 e 1
Numero_Aleatorio = random.random()
print(f'O Numero gerado foi: {Numero_Aleatorio} \n')

Numero_Aleatorio_01 = random.randint(0, 10)
print(f'Número aleatorio entre 1 e 10 foi: {Numero_Aleatorio_01}')