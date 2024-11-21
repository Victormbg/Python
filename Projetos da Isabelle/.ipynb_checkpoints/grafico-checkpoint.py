import matplotlib.pyplot as plt
import numpy as np

# Simulação de dados meteorológicos
dias = np.arange(1, 11)  # 10 dias
temperatura = [25, 26, 28, 27, 29, 30, 31, 33, 34, 35]
umidade = [60, 62, 58, 55, 57, 53, 52, 50, 48, 46]
pressao = [1012, 1013, 1010, 1008, 1011, 1010, 1007, 1005, 1006, 1004]
vento = [10, 15, 12, 20, 18, 22, 25, 30, 28, 35]
precipitacao = [0, 2, 0, 5, 10, 0, 0, 8, 15, 20]

# Criação do gráfico
plt.figure(figsize=(12, 6))

# Adicionando cada parâmetro ao gráfico
plt.plot(dias, temperatura, marker='o', label='Temperatura (°C)', color='red')
plt.plot(dias, umidade, marker='s', label='Umidade Relativa (%)', color='blue')
plt.plot(dias, pressao, marker='^', label='Pressão (hPa)', color='green')
plt.plot(dias, vento, marker='d', label='Vento (km/h)', color='purple')
plt.plot(dias, precipitacao, marker='x', label='Precipitação (mm)', color='orange')

# Configurações do gráfico
plt.title('Dados Meteorológicos ao Longo do Tempo', fontsize=16)
plt.xlabel('Dias', fontsize=14)
plt.ylabel('Valores', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.xticks(dias)
plt.tight_layout()

# Exibição do gráfico
plt.show()