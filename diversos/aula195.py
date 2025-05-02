import matplotlib.pyplot as plt  # Importa o módulo principal do Matplotlib

# Dados de exemplo (X e Y)
x = [1, 2, 3, 4, 5]  # Valores do eixo X
y = [10, 20, 25, 40, 30]  # Valores do eixo Y

# Cria uma figura e um eixo de plotagem
fig, ax = plt.subplots()  # `plt.subplots()` cria uma figura e um eixo para o gráfico

# Plota os dados com uma linha azul e marcadores de círculo
ax.plot(x, y, marker='o', linestyle='-', color='b', label='Dados')  
# `marker='o'` adiciona marcadores nos pontos dos dados
# `linestyle='-'` define a linha como sólida
# `color='b'` usa a cor azul
# `label='Dados'` define a legenda do gráfico

# Adiciona título e rótulos aos eixos
ax.set_title('Exemplo de Gráfico com Matplotlib')  # Define o título do gráfico
ax.set_xlabel('Eixo X')  # Define o rótulo do eixo X
ax.set_ylabel('Eixo Y')  # Define o rótulo do eixo Y

# Adiciona uma legenda
ax.legend()  # Mostra a legenda baseada na propriedade 'label' definida anteriormente

# Exibe o gráfico
plt.show()  # Exibe o gráfico na tela
