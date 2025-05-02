import pandas as pd  # Importa a biblioteca Pandas

# Criando um DataFrame com dados fictícios
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Idade': [25, 30, 22, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre'],
    'Salário': [5000, 7000, 4800, 6200]
}

df = pd.DataFrame(dados)  # Converte o dicionário em um DataFrame do Pandas

# Exibindo o DataFrame
print("DataFrame original:")
print(df)

# Filtrando apenas pessoas com idade maior que 25 anos
df_filtrado = df[df['Idade'] > 25]
print("\nPessoas com mais de 25 anos:")
print(df_filtrado)

# Adicionando uma nova coluna com aumento salarial de 10%
df['Salário Ajustado'] = df['Salário'] * 1.1
df['Comentário'] = 'Exemplo'
print("\nDataFrame com coluna adicional:")
print(df)

# Calculando estatísticas básicas
print("\nEstatísticas básicas:")
print(df.describe())  # Exibe estatísticas como média, desvio padrão e percentis

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)  # Exporta para CSV sem a coluna de índice

print("\nArquivo CSV gerado com sucesso!")
