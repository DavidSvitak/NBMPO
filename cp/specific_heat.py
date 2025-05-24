import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import pandas as pd
from scipy.signal import find_peaks
import re
data = pd.read_csv("Phase_diagram_boundary/NBMPO_along_ab.txt", header=0, sep=",", names=["T", "B", "B_T", "HC"], engine="python", encoding='unicode_escape')
data["HC"] = data["HC"]*1000
extremes = []
T = []
HC = []
first = data["B_T"][0]
#print(first)
#plt.figure()
for i in range(len(data)):
    if i == 3695:
        break
    if abs(data["B_T"][i]-first) < 0.01 and data["T"][i] < data["T"][i+1]:
        T.append(data["T"][i])
        HC.append(data["HC"][i])
    else:
        if len(T) == 0 and len(HC) == 0:
            first = data["B_T"][i]
        else:
            print(data["B_T"][i])
            first = data["B_T"][i]
            plt.plot(T, HC, "-", label = f"B = {round(data['B_T'][i-1], 4)} T")
            y_spl = UnivariateSpline(T,HC, s=0, k=4)
            y_spl_1d = y_spl.derivative(n=1)
            y_spl_2d = y_spl.derivative(n=2)
            x_range = np.linspace(T[0],T[-1],1000)
            for k, hodnota in enumerate(y_spl_1d(x_range)):
                if k == 0:
                    continue
                if hodnota*y_spl_1d(x_range)[k-1] <= 0 and y_spl_2d(x_range)[k] <= 0:
                    T_ex = round((x_range[k-1]+x_range[k])/2, 5)
                    B_ex = round(data["B_T"][i-1], 5)
                    HC_ex = y_spl(T_ex)
                    extremes.append([T_ex, B_ex, HC_ex])
                    plt.plot(T_ex, HC_ex, "ko")
            plt.legend()
            plt.figure()
            T = []
            HC = []
# 1.6 T measirement very wrong 

plt.figure()
pattern = re.compile(r'([^,]*),([^,]*),([^,]*)')
with open("Phase_diagram_boundary\extremes_along_ab.txt", "r") as txt:
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
plt.xlim((0.8, 1.5))
plt.ylim((0, 6))

with open("Phase_diagram_boundary/extremes_along_ab.txt", "w") as txt:
    txt.write("T(K), B(T), HC \n")
    for point in extremes:
        if point[0] < 1.5:
            txt.write(f"{point[0]}, {point[1]}, {point[2]} \n")

for point in extremes:
    if point[0] < 1.5:
        plt.plot(point[0], point[1], "ro")

plt.show()
