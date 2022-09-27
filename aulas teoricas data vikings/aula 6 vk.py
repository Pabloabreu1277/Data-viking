# 6º Tipo da Informação
# Na programação, o tipo de dados é um conceito importante. Variáveis podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes. O Python tem os seguintes tipos de dados integrados por padrão, nestas categorias:
#
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# Criando tipos de informações

String = str('Olá Mundo!')
Inteiro = int(10)
Flutuante = float(10.99)
Complex = complex(1j)
Lista = list( ('Maça', 'Morango', 'Pera') )
Tupla = tuple( ('Maça', 'Morango', 'Pera') )
Range = range(6)
Dicionario = dict(nome='Odemir', age=29)
Set = set( ('Maça', 'Morango', 'Pera') )
Fronzet = frozenset( ('Maça', 'Morango', 'Pera') )
Boleano = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
Memoryview = memoryview( bytes(5) )

from datetime import datetime
Data = datetime.today().date()

# Mostrando os Valores
print( type(String) )
print( type(Inteiro) )
print( type(Flutuante) )
print( type(Complex) )
print( type(Lista) )
print( type(Tupla) )
print( type(Range) )
print( type(Dicionario) )
print( type(Set) )
print( type(Fronzet) )
print( type(Boleano) )
print( type(Bytes) )
print( type(ByteArray) )
print( type(Memoryview) )
print( type(Data) )