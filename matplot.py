import matplotlib
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.title("Gráfico da Equação da Reta")
plt.plot(xpoints, ypoints)
plt.grid()
plt.show()

plt.savefig("matplot.png")