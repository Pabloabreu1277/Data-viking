# Importar as libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Ler os dados
Base_Dados = pd.read_csv('Startups in 2021 end.csv')

# Verificar Dimensão
Base_Dados.shape
print("="*30)
# Primeiros registros
print(Base_Dados.head())
print("="*30)
# Columnas
print(Base_Dados.columns)
print("="*30)
# Renomear
Base_Dados.rename( columns={
    'Unnamed: 0' : 'Id',
    'Company' : 'Empresa',
    'Valuation ($B)' : 'Valor ($)',
    'Date Joined' : 'Data de Adesão',
    'Country' : 'Pais',
    'City' : 'Cidade',
    'Industry': 'Setor',
    'Select Investors': 'Investidores',
}, inplace=True )

Base_Dados.info()

# Campos nulos
print(Base_Dados.isnull().sum())
print("="*30)
# Grafica
plt.figure( figsize=(15,6) )
plt.title('Analisando Campos Nulos')
sns.heatmap( Base_Dados.isnull(), cbar=False )
#Para visualizar o grafico habilite o comando abaixo
#plt.show()
print("="*30)
# Campos unicos
print(Base_Dados.nunique())
print("="*30)
# Valores Unicos
print(Base_Dados['Setor'].unique())
print("="*30)
# Valores Unicos - Rank
print(Base_Dados['Setor'].value_counts())
print("="*30)

# Valores Unicos - Rank
print(Base_Dados['Setor'].value_counts( normalize=True ))
print("="*30)

plt.figure( figsize=(15,6) )
plt.title('Analise dos Setores')
plt.bar( Base_Dados['Setor'].value_counts().index, Base_Dados['Setor'].value_counts()  )
plt.xticks( rotation=45, ha='right' )
#Para visualizar o grafico habilite o comando abaixo
#plt.show()
print("="*30)


Analise = round( Base_Dados['Pais'].value_counts( normalize=True ) * 100, 1 )

# Plot geral dos Paises
plt.figure( figsize=(15,6) )
plt.title('Analise dos Paises gerador de Unicornios')
plt.pie(
    Analise,
    labels = Analise.index,
    shadow=True,
    startangle=90,
    autopct='%1.1f%%'
)
#Para visualizar o grafico habilite o comando abaixo
#plt.show()
print("="*30)

# Conversão para Data
Base_Dados['Data de Adesão'] = pd.to_datetime( Base_Dados['Data de Adesão'] )

print(Base_Dados['Data de Adesão'].head())

print("="*30)

# Extrair o Ano e Mes
Base_Dados['Mes'] = pd.DatetimeIndex( Base_Dados['Data de Adesão'] ).month
Base_Dados['Ano'] = pd.DatetimeIndex( Base_Dados['Data de Adesão'] ).year

print(Base_Dados.head())
print("="*30)

# Tabela Analitica
Analise_Agrupada = Base_Dados.groupby( by=['Pais', 'Ano', 'Mes', 'Empresa'] ).count()['Id'].reset_index()

print(Analise_Agrupada)

print("="*30)

Analise_Agrupada1 = Analise_Agrupada.loc[
  Analise_Agrupada['Pais'] == 'Brazil'
]
print(Analise_Agrupada1)

print("="*30)

# Transformando a coluna Valor
Base_Dados['Valor ($)'] = pd.to_numeric( Base_Dados['Valor ($)'].apply( lambda Linha: Linha.replace('$', '') ) )

print(Base_Dados.head())
print("="*30)

# Tabela Analitica
Analise_Pais = Base_Dados.groupby( by=['Pais'] ).sum()['Valor ($)'].reset_index()

print(Analise_Pais.head())

Analise_Valor = Analise_Pais.sort_values('Valor ($)', ascending=False)
print(Analise_Valor.head())

print("="*30)

plt.figure( figsize=(15,7) )
plt.plot( Analise_Valor['Pais'], Analise_Valor['Valor ($)'] )
plt.title('Analise do Valor por Pais')
plt.xticks( rotation=45, ha='right')
plt.show()

