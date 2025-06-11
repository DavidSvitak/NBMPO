import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from ufit.lab import *
from ufit.plotting import mapping

#
### Plot of data of propagation vector
#
"""
set_datatemplate('6_9_2023_NI12/scan_data/070%03d')
#set_dataformat('ill')
data = read_numors('76-93', 0)
set_cmap("jet")
mapping("QH", "QL", data, mode=0, title="Magnetic peak at 55mK")
plt.savefig("6_9_2023_NI12/scan_data/Elastic_scattering_55mK.pdf")
plt.xlabel("(H,H,0) (r.l.u.)")
plt.ylabel("(0,0,L) (r.l.u.)")
plt.show()
"""
#
### Selection of data for propagation vector fitting
#

peak_tretina = []
peak_sestina = []
names = ["PNT", "QH", "QK", "QL", "EN", "M1", "TIME", "CNTS", "A2", "A3", "A3P", "A4", "KI", "KF", "RMH", "RA", "TT", "TRT", "MAG"]
for i in range(76,94):
    df = pd.read_csv(f"6_9_2023_NI12/scan_data/0700{i}", skiprows=51, sep="    ", names=names)
    for j in range(len(df["QH"])):
        if (0.05 < df["QL"][j] < 0.4) and (0.25 < df["QH"][j] < 0.4):
            points = [df["QH"][j], df["QL"][j], df["CNTS"][j]]
            peak_tretina.append(points)
        elif (0.05 < df["QL"][j] < 0.28) and (0.65 < df["QH"][j] < 0.7):
            points = [df["QH"][j], df["QL"][j], df["CNTS"][j]]
            peak_sestina.append(points)

with open("6_9_2023_NI12/scan_data/propagation_vector_third.txt", "w") as txt:
    txt.write("QH, QL, CNTS\n")
    for point in peak_tretina:
        txt.write(f"{point[0]}, {point[1]}, {point[2]}\n")

with open("6_9_2023_NI12/scan_data/propagation_vector_sixth.txt", "w") as txt:
    txt.write("QH, QL, CNTS\n")
    for point in peak_sestina:
        txt.write(f"{point[0]}, {point[1]}, {point[2]}\n")













