import math
import numpy as np
import matplotlib.pyplot as plt

print('Input N')
n = int(input())
print('Input M')
m = int(input())

X = np.random.sample((n, m))

pareto_front = np.empty([0, X.shape[1]])
not_pareto_front = np.empty([0, X.shape[1]])

temp_arr = np.empty([X.shape[1], 1])
temp_arr.fill(True)

for i in range(X.shape[0]):
    A = X[i] <= X

    if np.sum(A.dot(temp_arr) == X.shape[1]) > 1:
        not_pareto_front = np.vstack((not_pareto_front, X[i]))

    else:
        pareto_front = np.vstack((pareto_front, X[i]))

fig = plt.figure(figsize=[10, 10])

axs = fig.add_subplot(projection="polar")
axs.set_yticks([])
plt.thetagrids(np.arange(0, 360, 360.0 / X.shape[1]), labels=np.arange(0, X.shape[1], 1))

xPolar = np.arange(0, X.shape[1], 1)
xPolar = np.append(xPolar, 0)
xPolar = xPolar * 2 * math.pi / X.shape[1]

for x in not_pareto_front:
    yPolar = np.append(x, x[0])
    axs.plot(xPolar, yPolar, color="green")

for x in pareto_front:
    yPolar = np.append(x, x[0])
    axs.plot(xPolar, yPolar, color="red")

plt.show()
