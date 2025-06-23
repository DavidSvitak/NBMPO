import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from matplotlib.lines import Line2D

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

plt.plot([0.3, 0.3], [0,3.8], "k-", label="Scan",linewidth=3 ,linestyle=':')
plt.legend()
plt.xlabel("T(K)")
plt.ylabel("H(T)")
plt.ylim(0, 6)
plt.savefig("phase_diagrams_presentation/along_c_300mK.png")

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

plt.plot([1.2, 1.2], [0,3.8], "k-", label="Scan",linewidth=3 ,linestyle=':')
plt.legend()
plt.xlabel("T(K)")
plt.ylabel("H(T)")
plt.ylim(0, 6)
plt.savefig("phase_diagrams_presentation/along_c_1200mK.png")

plt.show()