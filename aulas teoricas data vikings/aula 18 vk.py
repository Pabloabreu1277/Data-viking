# 18° Pacote Externo - Time
# Este módulo fornece várias funções relacionadas ao tempo

# Importar a Lib
import time

print('Esse print foi rápido!')
time.sleep(2.5)
print('Esse print aconteceu depois de 2.5 segundos \n')

# Capturar o local agora
Agora = time.localtime()
print( type(Agora) )
print( Agora )
print( time.strftime('%m/%d/%Y, %H:%M:%S', Agora ), '\n' )

# Converter uma string para time
Time_Texto = '21 June, 2018'
Conversao = time.strptime(Time_Texto, '%d %B, %Y')
print(Conversao)