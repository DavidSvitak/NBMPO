import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import re

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
    y_err_n = []
    for line in txt:
        line = line.strip()
        tt, hh = line.split(",")
        if tt == "T(K)" and hh == "H(T)":
            continue
        tt = float(tt)
        hh = float(hh)
        x_data_n.append(tt)
        y_data_n.append(hh)
        y_err_n.append(0.1)
plt.errorbar(x_data_n, y_data_n,yerr=y_err_n,fmt= "bo", label = "Neutrons")

plt.legend()
plt.xlabel("T(K)")
plt.ylabel("H(T)")
plt.ylim(-0.1, 6)
plt.xlim(0.1, 1.5)
plt.plot([0.1, 1.5], [0,0], "k-", label="Scan",linewidth=3 ,linestyle=':')
plt.legend()
plt.savefig("phase_diagrams_presentation/ground_state.png")
plt.show()





