import plotly.graph_objects as go
import numpy as np
import cmath as cm

print("Hej, slyszalam, ze chcialbys zobaczyc wizualizacje funkcji czastki w pudelku potencjalu 3D. Swietnie trafiles :3")
print("Musisz najpierw podac mi liczby kwantowe dla wszystkich 3 wymiarow! Mozesz wybrac liczby w zakresie od 1 do 8 ;)")
nx = input("Podaj nx ")
nx = int(nx)
ny = input("Podaj ny ")
ny = int(ny)
nz = input("Podaj nz ")
nz = int(nz)

# wymiary pudelka potencjalu
Lx, Ly, Lz = 8, 8, 8
# objetosc pudelka
V = Lx*Ly*Lz
X, Y, Z = np.mgrid[0:Lx:40j, 0:Ly:40j, 0:Lz:40j]
# funkcja falowa czastki w pudelku potencjalu 3D
values = np.sqrt(8/V)*np.sin((nx*X*cm.pi)/Lx)*np.sin((ny*Y*cm.pi)/Ly)*np.sin((nz*Z*cm.pi)/Lz)

fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=0.01,
    isomax=0.1,
    opacity=0.05,
    surface_count=20,
    ))
fig.show()