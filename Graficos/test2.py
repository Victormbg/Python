import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(x, y)
ax.annotate("Maior valor", 
            xy=(10, 12),
            xycoords='data',
            xytext=(11, 10),
            textcoords='data',
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
plt.show()
