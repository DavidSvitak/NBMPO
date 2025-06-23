import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata
import re

### Along c axis

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
plt.colorbar(im, label=r'C$_{p}$ ($\mu $J$\cdot$K$^{-1}\cdot$mol$^{-1}$)')
plt.xlabel('T (K)')
plt.xlim(0.3, 1.5)
plt.ylim(0, 7)
plt.ylabel('H (T)')
plt.title(r'Magnetic field applied along the $c$ axis')
pattern = re.compile(r'([^,]*),([^,]*),([^,]*)')
x_data_cp = []
y_data_cp = []
with open("cp/extremes_along_c_specific_heat.txt", "r") as txt:
    for line in str.split(txt.read(), "\n"):
        line = line.strip()
        match = pattern.match(line)
        if match:
            tt, bb, hc = match.groups()
            if tt == "T(K)":
                continue
            else:
                x_data_cp.append(float(tt))
                y_data_cp.append(float(bb))
plt.plot(x_data_cp, y_data_cp, "ro", label = r"C$_p$")

with open("cp/H_along_c_transitions.txt", "r") as txt:
    x_data_n = []
    y_data_n = []
    for line in txt:
        line = line.strip()
        tt, hh = line.split(",")
        if tt == "T(K)" and hh == "H(T)":
            continue
        tt = float(tt)
        hh = float(hh)
        x_data_n.append(tt)
        y_data_n.append(hh)
plt.plot(x_data_n, y_data_n, "bo", label = "Neutrons")
plt.legend()
plt.text(0.4, 0.3, "AFM1")
plt.text(0.4, 1.1, "phase A")
plt.text(1.12, 0.3, "AFM2")
plt.text(0.8, 2, "UUD phase")
plt.savefig("cp/H_along_c_extremes_2.png")



### In the ab plane 


df = pd.read_csv("cp/along_ab.txt", names=["T","B_Oe","B","Cp"], sep=",", header=2, dtype=np.float64)

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
                origin='lower', cmap='viridis', aspect='auto', vmin=0, vmax=55)
plt.colorbar(im, label=r'C$_{p}$ ($\mu $J$\cdot$K$^{-1}\cdot$mol$^{-1}$)')
plt.xlabel('T (K)')
plt.xlim(0.3, 1.5)
plt.ylim(0, 7)
plt.ylabel('H (T)')
plt.title(r'Magnetic field applied along the $c$ axis')
pattern = re.compile(r'([^,]*),([^,]*),([^,]*)')
x_data_cp = []
y_data_cp = []
with open("cp/extremes_along_ab_specific_heat.txt", "r") as txt:
    for line in str.split(txt.read(), "\n"):
        line = line.strip()
        match = pattern.match(line)
        if match:
            tt, bb, hc = match.groups()
            if tt == "T(K)":
                continue
            else:
                x_data_cp.append(float(tt))
                y_data_cp.append(float(bb))
plt.plot(x_data_cp, y_data_cp, "ro", label = r"C$_p$")

with open("cp/H_along_ab_transitions.txt", "r") as txt:
    x_data_n = []
    y_data_n = []
    for line in txt:
        line = line.strip()
        tt, hh = line.split(",")
        if tt == "T(K)" and hh == "H(T)":
            continue
        tt = float(tt)
        hh = float(hh)
        x_data_n.append(tt)
        y_data_n.append(hh)
plt.plot(x_data_n, y_data_n, "bo", label = "Neutrons")
plt.legend()
plt.text(0.4, 0.3, "AFM1")
plt.text(0.4, 1.3, "phase C")
plt.text(0.4, 1.8, "phase D")
plt.text(0.4, 3, "phase E")
plt.text(1, 2.9, "AFM2")
plt.savefig("cp/H_along_ab_extremes_2.png")



plt.show()