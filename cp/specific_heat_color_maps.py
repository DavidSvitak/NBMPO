import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata
import re

df = pd.read_csv("cp/along_c.txt", names=["T","Cp","B"], sep=",", header=2, dtype=np.float64)

x = df['T'].values
y = df['B'].values
z = df['Cp'].values/1000

# 3. Create a regular 2D grid to interpolate onto
xi = np.linspace(x.min(), x.max(), 300)
yi = np.linspace(y.min(), y.max(), 300)
X, Y = np.meshgrid(xi, yi)

# 4. Interpolate z values onto the grid
Z = griddata((x, y), z, (X, Y), method='linear')  # or 'linear'/'nearest'

# 5. Plot the result
plt.figure(figsize=(7, 6))
im = plt.imshow(Z, extent=(x.min(), x.max(), y.min(), y.max()),
                origin='lower', cmap='viridis', aspect='auto', vmin=0, vmax=20)
plt.colorbar(im, label=r'C$_{p}$ ($\mu $J$\cdot$K$^{-1}$)')
plt.xlabel('T (K)')
plt.xlim(0.6, 1.5)
plt.ylim(0.4, 7)
plt.ylabel('H (T)')
plt.title(r'Magnetic field applied along the $c$ axis')
pattern = re.compile(r'([^,]*),([^,]*),([^,]*)')
with open("cp/extremes_along_c_specific_heat.txt", "r") as txt:
    for line in str.split(txt.read(), "\n"):
        line = line.strip()
        match = pattern.match(line)
        if match:
            tt, bb, hc = match.groups()
            if tt == "T(K)":
                continue
            else:
                tt = float(tt)
                bb = float(bb)
                plt.plot(tt, bb, "ro")
plt.savefig("cp/H_along_c_extremes.png")

plt.show()