import matplotlib.pyplot as plt

'''
COMENTARIO
plt.plot(x, y) #Criando o gráfico
plt.title('SEU TÍTULO LINDO') #adicionando o título
plt.xlabel('NOME DO EIXO X')
plt.ylabel('NOME DO EIXO Y')
plt.show()
'''

plt.title('VictorManuel')
radius = [1.0, 2.0, 3.0, 4.0]
area = [3.14159, 12.56636, 28.27431, 50.26544]
plt.plot(radius, area)
plt.show()
