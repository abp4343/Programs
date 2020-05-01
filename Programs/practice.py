import matplotlib.pyplot as plt
import numpy as np

delta_X = np.random.normal(0, 1, (2, 100000))
X = np.cumsum(delta_X, axis = 1)
X_0 = np.array([[0], [0]])
X = np.concatenate((X_0, X), axis = 1)
plt.plot(X[0], X[1], "ro-", markersize = 0.1)