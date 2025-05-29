import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata

df = pd.read_csv("cp/along_ab.txt", names=["T","1","B","Cp"], sep=",", header=2, dtype=np.float64)

x = df['T'].values
y = df['B'].values
z = df['Cp'].values

# 3. Create a regular 2D grid to interpolate onto
xi = np.linspace(x.min(), x.max(), 300)
yi = np.linspace(y.min(), y.max(), 300)
X, Y = np.meshgrid(xi, yi)

# 4. Interpolate z values onto the grid
Z = griddata((x, y), z, (X, Y), method='linear')  # or 'linear'/'nearest'

# 5. Plot the result
plt.figure(figsize=(7, 6))
im = plt.imshow(Z, extent=(x.min(), x.max(), y.min(), y.max()),
                origin='lower', cmap='viridis', aspect='auto', vmin=0, vmax=60)
plt.colorbar(im, label=r'C$_{p}$ ($\mu $J$\cdot$K$^{-1}$)')
plt.xlabel('T (K)')
plt.xlim(0.6, 1.5)
plt.ylim(0, 7)
plt.ylabel('H (T)')
plt.title(r'Magnetic field applied in the $ab$ plane')
plt.savefig("cp/H_along_ab.png")

plt.show()