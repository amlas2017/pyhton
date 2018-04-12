import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi*10, np.pi*10, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X,C, color="blue", linewidth=2.5)
plt.plot(X,S, color="red", linewidth=5)
plt.show()