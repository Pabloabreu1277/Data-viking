# 14º Operadores de Identidade
# Os operadores de identidade são usados ​​para comparar os objetos, não se forem iguais, mas se forem realmente o mesmo objeto, com a mesma localização de memória:
#
# is (Retorna True se ambas as variáveis ​​forem o mesmo objeto)
# is not (Retorna True se ambas as variáveis ​​não forem o mesmo objeto)]

String_01 = str('Olá Mundão')
String_02 = str('Olá Mundão')

print( String_01 is String_01 )
print( String_01 is String_02 )
print( String_01 == String_02 )
print( type(String_01) is type(String_02) )