import numpy as np
import matplotlib.pyplot as plt

N = 128

x_0 = 2
h = x_0 / N

dt = 1e-5
t_0 = 1.15
M = int(t_0 / dt) + 1
print(M)

delta = 0.022

x = np.linspace(0, x_0, N, endpoint=False)

print(h, x[0:3])

u = np.zeros((M, N))

u[0] = np.cos(np.pi * x)

for i in range(N):
    u[1][i] = u[0][i] - 1/3 * dt/2/h * (u[0][(i + 1)%N] + u[0][i] + u[0][(i - 1)%N]) * (u[0][(i + 1)%N] - u[0][(i - 1)%N]) - delta**2 * dt/2 / h**3 * (u[0][(i + 2)%N] - 2 * u[0][(i + 1)%N] + 2 * u[0][(i - 1)%N] - u[0][(i - 2)%N])

for j in range(1, M-1):
    for i in range(N):
        u[j + 1][i] = u[j - 1][i] - 1/3 * dt/h * (u[j][(i + 1)%N] + u[j][i] + u[j][(i - 1)%N]) * (u[j][(i + 1)%N] - u[j][(i - 1)%N]) - delta**2 *dt / h**3 * (u[j][(i + 2)%N] - 2 * u[j][(i + 1)%N] + 2 * u[j][(i - 1)%N] - u[j][(i - 2)%N])

# for i in range(0,M,99):
#     plt.plot(x, u[i])
plt.plot(x, u[M-3])

plt.savefig("smth.png")