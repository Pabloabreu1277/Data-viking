#Part 1
#Referencia:https://www.youtube.com/watch?v=ubCBOYcj-4w&list=PLLWTDkRZXQa9YyC1LMbuDTz3XVC4E9ZQA&index=57
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

#lendo base de dados
base_dados = pd.read_csv('StudentsPerformance.csv')

#dimensão
print(base_dados.shape)
print('#'*165)

#head
print(base_dados.head())
print('#'*165)

#campos nulos
nulo = base_dados.isnull()
plt.figure(figsize=(16,5))
plt.title('Analise de campos nulos')
#sns.heatmap(nulo, cbar=False)
#plt.show()
print(nulo.sum())
print('#'*165)

#dados unicos
print(base_dados.nunique())
print('#'*165)

#campos duplicados
print("Campos duplicados: ",base_dados.duplicated().sum())
print('#'*165)

# estatistica
print(base_dados.describe())
print('#'*165)

#info dos dados
print(base_dados.info())
print('#'*165)

#Part 2
#Referencia:https://www.youtube.com/watch?v=lwxFNgGVWBQ&list=PLLWTDkRZXQa9YyC1LMbuDTz3XVC4E9ZQA&index=58

#gender genero sexual
print(base_dados['gender'].value_counts(normalize=True )*100)
print('#'*165)
#raça/etnia
print(base_dados['race/ethnicity'].value_counts(normalize=True )*100)
print('#'*165)
#nível de escolaridade dos pais
print(base_dados['parental level of education'].value_counts(normalize=True )*100)
print('#'*165)
#CAndidato almoçou padrão ou algo diferente
print(base_dados['lunch'].value_counts(normalize=True )*100)
print('#'*165)
#Teste preparatorio
print(base_dados['test preparation course'].value_counts(normalize=True )*100)
print('#'*165)
"""
#Comparação de variaveis com as notas matematica x genero
comp_matgen=sns.boxplot(data=base_dados, x='math score',y='gender')
comp_matgen.set_title("Comparação nota de matematica X Genero")
#plt.show()
#Comparação de variaveis com as notas leitura x genero
comp_leigen=sns.boxplot(data=base_dados, x='reading score',y='gender')
comp_leigen.set_title("Comparação nota de leitura X Genero")
#plt.show()
#Comparação de variaveis com as notas redação x genero
comp_redgen=sns.boxplot(data=base_dados, x='writing score',y='gender')
comp_redgen.set_title("Comparação nota de redação X Genero")
#plt.show()
"""


#parte 3
#referencia: https://www.youtube.com/watch?v=6zg122giHR8&list=PLLWTDkRZXQa9YyC1LMbuDTz3XVC4E9ZQA&index=59

#Agrupamento de dados para comparação por genero na matematica
print(base_dados.groupby(by=['gender']).describe()['math score'].reset_index())
print('#'*165)



#grade de dados da base 
#grade = sns.pairplot(base_dados, hue='race/ethnicity')
#grade.set_title("grade com as comparações")
#plt.show()

#caixa1 = sns.boxplot( data = base_dados, x='math score', y='race/ethnicity')
#caixa1.set_title("Grafico comparando notas de matematica x etinias")
#plt.show()

#caixa2 = sns.boxplot( data = base_dados, x='math score', y='parental level of education')
#caixa2.set_title("Grafico comparando notas de matematica x educação pais")
#plt.show()

#Agrupamento de dados para comparação por educação dos pais na matematica
print(base_dados.groupby(by=['parental level of education']).describe()['math score'].reset_index())
print('#'*165)

#caixa3 = sns.boxplot( data = base_dados, x='math score', y='test preparation course')
#caixa3.set_title("Grafico comparando notas de matematica x curso preparatorio")
#plt.show()

#Agrupamento de dados para comparação por curso preparatorio na matematica
print(base_dados.groupby(by=['test preparation course']).describe()['math score'].reset_index())
print('#'*165)

caixa4 = sns.scatterplot( data = base_dados, x='math score', y='writing score')
caixa4.set_title("Grafico comparando notas de matematica x nota de redação")
plt.show()

#Conclusão
#para desabilitar os graficos retire "#" do comando plt.show(), e dos comandos do sns.
# Avaliando os dados desse projeto verificamos que quando o aluno se prepara ele vai melhor nas provas.
# A influencia da formação dos pais colabora para um melhro resultado conforme avaliamos pois a cultura familiar influencia para isso.
# em relação a etnia e o genero não obtvemos conclusões predominantes.
