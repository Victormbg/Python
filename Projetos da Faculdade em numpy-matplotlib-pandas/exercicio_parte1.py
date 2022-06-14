from matplotlib import pyplot

CVP_Estatura = (5/175)*100
CVP_Peso = (2/68)*100

print(round(CVP_Estatura, 2))

#plot
pyplot.scatter(CVP_Estatura,CVP_Peso)
pyplot.title('Gráfico de Dispersão entre CVP da Estatura e CVP do Peso')
pyplot.show()

