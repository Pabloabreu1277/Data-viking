# 23º Estrutura de Loop FOR
# O loop For do Python é usado para travessia seqüencial, ou seja, é usado para iterar sobre um iterável como string, tupla, lista, etc. Ele se enquadra na categoria de iteração definida . Iterações definidas significam que o número de repetições é especificado explicitamente com antecedência.

for variável in objeto:

loop
# For [ Loop ]

for QualquerCoisaQueVoceQuiser in range(10):
  print( QualquerCoisaQueVoceQuiser ** 2  )

  # For + Lista

  Lista_Paises = ['Brasil', 'Argentina', 'Uruguai', 'Chile', 'Paraguai', 'Bolivia', 'Equador',
                  'Colombia', 'Suriname', 'Guiane', 'Goianai France']

  for Loop in Lista_Paises:
    print(Loop)

    # For + Lista
    Lista_Paises = ['Brasil', 'Argentina', 'Uruguai', 'Chile', 'Paraguai', 'Bolivia',
                    'Equador', 'Colombia', 'Suriname, Guiane, Goianai France']

    for Loop in range(len(Lista_Paises)):
      print(Lista_Paises[Loop])

  # For + Lista + IF + enumerate
  for Posicao, P in enumerate(Lista_Paises):
    print(Posicao / 4, P)
# for + LISTa + IF + RANGE
Lista_Numerica = [ Numero for Numero in range(1, 100, 5) ]
Armazenar = []

for x in Lista_Numerica:

  if x % 2 == 0:
    Armazenar.append( x )

print( Armazenar )

from pandas import DataFrame
print( DataFrame(Armazenar) )

# For + Lista + Dicionario

Lista = [ 'Brasil', 'Argentina', 'Uruaguai', 'Paraguai' ]

Dicionario = {
    'Brasil' : 'Real',
    'Argentina' : 'Peso ARG',
    'Uruaguai' : 'Peso URU',
    'Paraguai' : 'Guarany'
}

for Paises in Lista:

  if Paises == 'Brasil':
    print( f'Moeda do {Paises} é { Dicionario[Paises] }' )
    print('Mooeda do', Paises, 'é', Dicionario[Paises] )
    print('Mooeda do ' + str (Paises) + ' é ' + str(Dicionario[Paises] ) )
  else:
    pass