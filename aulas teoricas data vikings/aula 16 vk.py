# 16º Manipulando Listas
# As listas são usadas para armazenar vários itens em uma única variável.
#
# As listas são um dos 4 tipos de dados internos do Python usados ​​para armazenar coleções de dados, os outros 3 são Tuple , Set e Dictionary , todos com qualidades e usos diferentes.
#
# Comandos mais utilizados:
#
# append() - Para adicionar um item ao final da lista
# len() - Calcular o tamanho da lista
# [ ] - Acessar posições
# del() - Exlcuir um elemtno
# clear() - Limpar a lista
# insert() - Para inserir um item de lista em um índice especificado
# extend() - Anexar elementos de outra lista à lista atual
# remove() - Remove o item especificado
# pop() - Remove o índice especificado.
# sort() - Ordenar os valores
# copy() - Faz uma copia da Lista
# index() - Retorna o index do elemento da lista
# Manipulando dados dentro das Lista
Lista_Vazia = []
print('Lista antes:', Lista_Vazia, '\n' )

# Inserindo valores na Lista
Lista_Vazia.append(1)
Lista_Vazia.append(2)
Lista_Vazia.append(3)
print('Lista Depois:', Lista_Vazia, '\n' )

# Tamanho da lista
print('Lista contém:', len(Lista_Vazia), 'elementos', '\n' )

# Tamanho da lista
print('Acessando o 1º Elemento:', Lista_Vazia[0] )
print('Acessando o 2º Elemento:', Lista_Vazia[1] )
print('Acessando o último Elemento:', Lista_Vazia[-1] )
print('Acessando um periodo:', Lista_Vazia[0:2], '\n' )

# Excluindo valor na lista
del Lista_Vazia[1]
print('Depois da exclusão:', Lista_Vazia, '\n' )

# Limpando a lista
print('Depois da Limpeza:', Lista_Vazia.clear(), '\n' )

# Inserindo um valor com uma posição
Lista_Inserir = ['Posição 1', 'Posição 2', 'Posição 3']
Lista_Inserir.insert( 0, 'Posição 4' )
print( Lista_Inserir, '\n' )

# Inserindo uma lista na outra
Lista_Inserir_01 = ['Posição 1', 'Posição 2', 'Posição 3']
Lista_Inserir_02 = ['Posição 4', 'Posição 5', 'Posição 6']
Lista_Inserir_01.extend( Lista_Inserir_02 )
print( Lista_Inserir_01, '\n' )

# Removendo itens especifico pelo nome
Lista_Inserir_01.remove('Posição 6')
print( Lista_Inserir_01, '\n' )

# Removendo itens pelo index
Lista_Inserir_01.pop(0)
print( Lista_Inserir_01, '\n' )

# Ordenar uma lista
Lista_Alfabetica = ['Z', 'C', 'A', 'B', 'L']
Lista_Alfabetica.sort()
print( Lista_Alfabetica, '\n' )

# Ordenar uma lista de forma inversa
Lista_Alfabetica.sort( reverse=True )
print( Lista_Alfabetica, '\n' )

# Copiar uma Lista
Lista_Alfabetica_02 = Lista_Alfabetica.copy()
print( Lista_Alfabetica_02, '\n' )

# Indetificar o Index do elemtno na lista
print( Lista_Alfabetica_02.index('L'), '\n' )