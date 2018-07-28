#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
import matplotlib.pyplot as plt
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.axes([0.025, 0.025, 0.095, 0.095])

plt.plot(X, Y + 1, color='green', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='black', alpha=.25)

plt.plot(X, Y - 1, color='red', alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='yellow', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='black',  alpha=.25)

plt.xlim(-np.pi, np.pi)
plt.xticks(())
plt.ylim(-2.5, 2.5)
plt.yticks(())

plt.show()
