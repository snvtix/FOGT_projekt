import plotly.graph_objects as go
import numpy as np
import cmath as cm

nx = 1
ny = 1
nz = 4
Lx = 8
Ly = 8
Lz = 8
V = Lx*Ly*Lz
X, Y, Z = np.mgrid[-Lx:Lx:40j, -Ly:Ly:40j, -Lz:Lz:40j]
values = np.sqrt(8/V)*np.sin((nx*X*cm.pi)/Lx)*np.sin((ny*Y*cm.pi)/Ly)*np.sin((nz*Z*cm.pi)/Lz)

fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=0.05,
    isomax=0.2,
    opacity=0.2, # needs to be small to see through all surfaces
    surface_count=17, # needs to be a large number for good volume rendering
    ))
fig.show()