import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')

# RQ 01: Boxplot - Idade do repositório
plt.figure(figsize=(8, 6))
plt.boxplot(df['Age'])
plt.title('RQ 01: Idade do Repositório')
plt.ylabel('Dias desde a criação')
plt.show()

# RQ 02: Boxplot - Total de pull requests aceitas
plt.figure(figsize=(8, 6))
plt.boxplot(df['Pull Requests'])
plt.title('RQ 02: Total de Pull Requests Aceitas')
plt.ylabel('Número de Pull Requests')
plt.show()

# RQ 03: Boxplot - Total de releases
plt.figure(figsize=(8, 6))
plt.boxplot(df['Releases'])
plt.title('RQ 03: Total de Releases')
plt.ylabel('Número de Releases')
plt.show()

# RQ 04: Boxplot - Tempo até a última atualização
plt.figure(figsize=(8, 6))
plt.boxplot(df['Days Since Update'])
plt.title('RQ 04: Tempo até a Última Atualização')
plt.ylabel('Dias desde a última atualização')
plt.show()

# RQ 05: Gráfico de barra - Linguagem primária
language_counts = df['Language'].value_counts()[:10]
plt.figure(figsize=(10, 6))
language_counts.plot(kind='bar')
plt.title('RQ 05: Linguagens Primárias dos Repositórios Populares (Top 10)')
plt.xlabel('Linguagem')
plt.ylabel('Número de Repositórios')
plt.xticks(rotation=45)
plt.show()

# RQ 06: Boxplot - Razão entre número de issues fechadas pelo total de issues
plt.figure(figsize=(8, 6))
plt.boxplot(df['Issues Ratio'])
plt.title('RQ 06: Razão entre número de Issues Fechadas pelo Total de Issues')
plt.ylabel('Razão (Closed Issues / Total Issues)')
plt.show()