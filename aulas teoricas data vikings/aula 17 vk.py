# 17º Pacote Externo - Datetime
# O datetime módulo fornece classes para manipulação de datas e horas.

import datetime

# Dia de Hoje
Dia_Hoje = datetime.datetime.today().date()
print( f'Hoje é: {Dia_Hoje} \n' )

# Construindo uma Data
Data = datetime.date(2020, 10, 1)
print( f'Construindo uma Data {Data} \n' )

# Acessando os atributos da DAta
Ano = Data.year
Mes = Data.month
Dia = Data.day
print(f'Hoje é dia {Dia} do mês {Mes} do ano de {Ano} \n')

# Operação
Intervalo = Data - Dia_Hoje
print(f'Já ocorreu {Intervalo} dias \n' )

# Ajustando o formato
Novo_Formato = Dia_Hoje.strftime('%d/%m/%y')
print( f'Hoje é: {Novo_Formato} \n' )

# Aumentar dias ou diminuir
print( f'Somando 30 dias, {Dia_Hoje + datetime.timedelta(days = 30)}' )
print( f'Diminuindo 30 dias, {Dia_Hoje - datetime.timedelta(days = 30)}' )