# 21° Pacote Externo - Statistics
# Este módulo fornece funções para calcular estatísticas matemáticas de dados numéricos e interage com as listas

# Importando a Statistics para operar nas listas
import statistics

# Retirando a média
Media = statistics.mean( [1, 2, 3, 4, 4] )
print(f'A media seria: {Media} \n')

Mediana = statistics.median( [1, 2, 3, 4, 4] )
print(f'A mediana seria: {Mediana} \n')

Moda = statistics.mode( [1, 2, 3, 4, 4] )
print(f'A moda seria: {Moda}')