import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from ufit.lab import *
from ufit.plotting import mapping
from scipy.optimize import curve_fit

set_datatemplate('6_9_2023_NI12/K_point/070%03d')


def line(x, a, b):
    return a*x + b

x_data = []
y_data = []
y_err = []
for i in range(228, 235):
    data = read_data(i, "EN", "CNTS")
    model = Background() + Gauss('p1', pos = 0.45, ampl=200, fwhm=0.1)
    model.fit(data)
    model.plot(data)
    x = data["QL"]
    print(x)
    y = model.params[1].value
    yerr = model.params[3].value/2
    x_data = np.append(x_data, [x], axis = 0)
    y_data = np.append(y_data, [y], axis = 0)
    y_err = np.append(y_err, [yerr], axis=0)
    data.plot()

fig = plt.figure()
data = read_numors('228-234', 0)
parameters, covariance = curve_fit(line, x_data, y_data)
fit_A = parameters[0]
err_A = covariance[0]
fit_B = parameters[1]
err_B = covariance[1]
print(f"{fit_A=}")
print(f"{err_A=}")
print(f"{fit_B=}")
print(f"{err_B=}")
#fit_C = parameters[2]
x_fit = np.linspace(-0.5, 0.5, 100)
fit_y = line(x_fit, fit_A, fit_B) #, fit_C)
mapping("QL", "EN", data, minmax=[0, 1500], label="Intensity (arb. unit)")
plt.title('')
plt.xlabel("(1/3, 1/3, L) (r.l.u.)")
plt.ylabel("E(meV)")
plt.errorbar(x_data, y_data,y_err, fmt='ro', label='Positions of Gaussian maxima')
plt.plot(x_fit, fit_y, 'r-', label="Dispersion in (0,0,Ql) direction")
plt.legend()
plt.savefig("6_9_2023_NI12\K_point\K_point.png", dpi=600)
plt.show()
