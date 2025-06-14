import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from matplotlib.lines import Line2D

# Along c axis 
fig, ax = plt.subplots()
pattern = re.compile(r'([^,]*),([^,]*),([^,]*)')
with open("cp/extremes_along_c_specific_heat.txt", "r") as txt:
    x_data_cp = []
    y_data_cp = []
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
plt.xlabel("T(K)")
plt.ylabel("H(T)")
plt.ylim(0, 6)
plt.text(0.6, 0.3, "AFM1")
plt.text(0.4, 1.1, "phase A")
plt.text(1.15, 0.3, "AFM2")
plt.text(0.8, 2, "UUD phase")
plt.title(r"Magnetic phase diagram with magnetic field applied along $c$ axis")
plt.savefig("cp/whole_diagram_c.png")

fig, ax = plt.subplots()
pattern = re.compile(r'([^,]*),([^,]*),([^,]*)')
with open("cp/extremes_along_ab_specific_heat.txt", "r") as txt:
    x_data_cp = []
    y_data_cp = []
    for line in str.split(txt.read(), "\n"):
        line = line.strip()
        match = pattern.match(line)
        if match:
            tt, bb, hc = match.groups()
            if tt == "T(K)":
                continue
            else:
                x_data_cp.append(float(tt)-0.04)
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
plt.xlabel("T(K)")
plt.ylabel("H(T)")
plt.ylim(0, 6)
plt.text(0.6, 0.3, "AFM1")
plt.text(0.4, 1.4, "phase C")
plt.text(1.05, 2.5, "AFM2")
plt.text(0.4, 2, "phase D")
plt.text(0.4, 3.2, "phase E")
plt.title(r"Magnetic phase diagram with magnetic field applied in the $ab$ plane")
plt.savefig("cp/whole_diagram_ab.png")
plt.show()

plt.show()