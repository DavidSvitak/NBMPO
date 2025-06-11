import numpy as np
import matplotlib.pyplot as plt
from ufit.lab import *
from ufit.plotting import mapping
import pandas as pd
from scipy.optimize import curve_fit
set_datatemplate('6_9_2023_NI12/spin_polarized_state/070%03d')




x_data = []
y_data = []
y_err = []
numbers = [215,216,217,222,223,224,225,226,227,243,244,245,246,247,248,249,250,251,252,253,254,255,256,261]
pos_expected = []
"""
for num in numbers:
    data = read_data(num, xcol = "EN", ycol = "CNTS")
    data.plot()
    model = Background() + Gauss("p1", pos = 0.5, ampl = 200, fwhm = 0.1)
    model.fit(data)
    model.plot(data)
    x = data["QH"]
    y = model.params[1].value
    yerr = model.params[3].value/3
    x_data = np.append(x_data, [x], axis = 0)
    y_data = np.append(y_data, [y], axis = 0)
    y_err = np.append(y_err, [yerr], axis=0)
"""

def energy(k_x, J, B_star):
    S = 5/2
    # - 6*S*J_prime
    return 2*S*J*(np.cos(2*np.pi*k_x) + 2*np.cos(np.pi*k_x)*np.cos(np.pi*k_x + 2*np.pi*k_x)) + B_star
    # B_star = spin * landau factor * moment of Mn * field = 10 T;  

df = pd.read_csv('6_9_2023_NI12/spin_polarized_state/plot_data.txt', sep = "    ", names=["x", "y", "yerr"], engine='python')
x_data = np.asarray(df['x'])
y_data = np.asarray(df['y'])
y_err = np.asarray(df['yerr'])
#plt.plot(x_data, y_data, 'ro')
parameters, covariance = curve_fit(energy, x_data, y_data)
fit_A = parameters[0]
err_A = covariance[0]
fit_B = parameters[1]
err_B = covariance[1]
print(f"{fit_A=}")
print(f"{err_A=}")
print(f"{fit_B=}")
print(f"{err_B=}")
#fit_C = parameters[2]
x_fit = np.linspace(0, 1, 100)
fit_y = energy(x_fit, fit_A, fit_B) #, fit_C)
plt.errorbar(x_data, y_data, yerr=y_err, fmt='o', label='data')
plt.plot(x_fit, fit_y, '-')  # , J_prime={fit_C:.2f}')
plt.legend()
plt.show()

fig = plt.figure()
data = read_numors('215,216,222-226, 243-256', 0)
data.name = ''
mapping('QH', 'EN', data, mode=0, title=f'{data.name}', minmax=[0, 1000], label="Intensity (arb. unit)")
plt.xlabel('(Qh,Qh,0) (r.l.u.)')
plt.ylabel('E(meV)')
plt.xlim((0.2, 0.5))
plt.ylim((0, 1))
plt.errorbar(x_data, y_data, yerr=y_err, fmt='bo', label='Positions of Gaussian maxima')
plt.plot(x_fit, fit_y, 'b-', label="Magnon dispersion")  # , J_prime={fit_C:.2f}')
plt.legend()
plt.savefig("6_9_2023_NI12\spin_polarized_state\spin_polarized__state.png", dpi=600)
plt.show()



