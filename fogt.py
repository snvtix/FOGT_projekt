import matplotlib.pyplot as plt
import numpy as np

# ustawiamy wymiary pudełka
Lx = 10
Ly = 10
Lz = 10

# tworzymy siatkę dla współrzędnych
x = np.linspace(0, Lx, 100)
y = np.linspace(0, Ly, 100)
z = np.linspace(0, Lz, 100)

# obliczamy wartość funkcji w każdym punkcie na siatce
V = np.zeros((100, 100, 100))
for i in range(100):
    for j in range(100):
        for k in range(100):
            V[i,j,k] = x[i]**2 + y[j]**2 + z[k]**2

# rysujemy wykres przestrzeni stanów
plt.figure()
plt.imshow(V[:,:,0], cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Przestrzeń stanów')

# rysujemy wykres wartości funkcji
plt.figure()
plt.imshow(V[:,:,0], cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wartość funkcji')

plt.show()