import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from matplotlib.lines import Line2D


# Specific heat
fig, ax = plt.subplots()
pattern = re.compile(r'([^,]*),([^,]*),([^,]*)')
with open("Phase_diagram_boundary\extremes_along_ab_specific_heat.txt", "r") as txt:
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

pattern = re.compile(r"([^,]*),([^,]*),([^,]*),([^,]*),([^,]*),([^,]*)")
with open("Phase_diagram_boundary\extremes_along_ab_neutrons.txt") as txt:
    for line in str.split(txt.read(), "\n"):
        line = line.strip()
        match = pattern.match(line)
        if match:
            tt, h1, h2, h3, h4, h5 = match.groups()
            if tt == "T":
                continue
            else:
                for h in [h1, h2, h3, h4, h5]:
                    if h :
                        tt = float(tt)
                        h = float(h)
                        plt.plot(tt, h, "bo")

ankit_data = pd.read_csv("Phase_diagram_boundary\sketch_H_par_ab.dat", header=1, names=["H", "T1", "T2"], sep=",")
for i in range(len(ankit_data)):
    plt.plot(ankit_data["T1"][i], ankit_data["H"][i], "ko")
    if ankit_data["T1"][i]:
        plt.plot(ankit_data["T2"][i], ankit_data["H"][i], "ko")



legend_elements = [
    Line2D([0], [0], marker="o", color="w", label="David data treatment", markerfacecolor='r', markersize=7),
    Line2D([0], [0], marker="o", color="w", label="Neutrons", markerfacecolor='b', markersize=7),
    Line2D([0], [0], marker="o", color="w", label="Ankit data treatment", markerfacecolor='k', markersize=7)
    ]


ax.legend(handles=legend_elements)
plt.savefig("Phase_diagram_boundary/Data_treatment_comparison_ab.jpg")
plt.show()