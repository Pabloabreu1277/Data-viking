# 27º Estrutura Lambda
# Uma função lambda é uma pequena função anônima.
#
# Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.

# Função
Funcao = lambda valor: valor + 10
print( Funcao( 10 ) )

Funcao_02 = lambda valor1, valor2 : valor1 + valor2
print( Funcao_02( 100 , 100 ) )
# Função Lambda
Nao_Faxa_isso = lambda Qualquer_Valor: 'Verdadeiro' if Qualquer_Valor % 2 == 0 else 'Falso'
#Nao_Faxa_isso = lambda x: True if x % 2 == 0 else Falso
Nao_Faxa_isso( 100 )