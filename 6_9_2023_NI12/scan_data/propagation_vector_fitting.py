import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from ufit.lab import *
from ufit.plotting import mapping
import re
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def fitting(x, y, z0, A1, x01, y01, w11, w12, A2, x02, y02, w21, w22):
    return z0 + A1*np.exp(-1/2*((x-x01)/w11)**2 - 1/2*((y-y01)/w12)**2) + A2*np.exp(-1/2*((x-x02)/w21)**2 - 1/2*((y-y02)/w22)**2)

x = []
y = []
z = []
pattern = re.compile(r'([^,]*), ([^,]*), ([^,]*)')
with open("6_9_2023_NI12/scan_data/propagation_vector_third.txt", "r") as txt:
    for line in txt.readlines():
        line = line.strip()
        match = pattern.match(line) 
        if match:
            QH, QL, counts = match.groups()
            if QH == "QH" and QL == "QL" and counts == "CNTS":
                pass
            else:
                QH = float(QH)
                QL = float(QL)
                counts = float(counts)
                x.append(QH)
                y.append(QL)
                z.append(counts)

plt.show()
