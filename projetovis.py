# Importação das bibliotecas.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Gráfico 01 - Linhas

#Leitura do dataset com a biblioteca pandas.
mt = pd.read_csv(r"C:\Users\henri\Documents\Projeto\dados_ipea.csv", parse_dates=True, sep=';')

#Utilização do método loc para encontrar o estado, período, valor de suicídios da região SUL.
M_PR = mt.loc[mt['estado']=="PR"] 
M_SC = mt.loc[mt['estado']=="SC"]
M_RS = mt.loc[mt['estado']=="RS"]

#Criação e Plotagem do Gráfico 01.
plt.figure(figsize=(15,5))

plt.plot(M_PR.periodo, M_PR.valor)
plt.plot(M_SC.periodo, M_SC.valor)
plt.plot(M_RS.periodo, M_RS.valor)

plt.xticks(mt.periodo)
plt.title("Suicídios - Arma de Fogo")
plt.legend(('PR','SC','RS'))
plt.xlabel('Ano')
plt.ylabel('Mortes')
plt.show()

#Gráfico 02 - Pizza

#Criação e Plotagem do Gráfico 02 com MATPLOTLIB e NUMPY.
plt.figure(figsize=(5,5))

labels = 'PR','SC','RS'
sizes = [2112,1219,4751] #Valor inserido com a técnica Hard-Code.
colors = [ 'lightgray', 'orange', 'coral', 'red'] 
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)
plt.legend(patches, labels, loc="lower right")
plt.title('Suicídios - Arma de Fogo')
plt.axis('equal')

plt.show()

#Gráfico 03 - Barras

#Criação e Plotagem do Gráfico 03 com MATPLOTLIB.
plt.figure(figsize=(5,5))

estados = ('SC','PR','RS')
indice = np.arange(len(estados))
mortes = [1219,2112,4751] 
plt.bar(indice, mortes, color = ("gray","yellow","red",(0.5,0.7,1.0)))
plt.xticks(indice, estados)
plt.ylabel('Suicídios')
plt.xlabel('Estados')
plt.title('Suicídios - Arma de Fogo')

plt.show()


































