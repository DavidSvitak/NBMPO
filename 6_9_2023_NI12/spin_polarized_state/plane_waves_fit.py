import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

def energy(k_x, J, B_star, B = 0):
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
fit_Mn = energy(x_fit, 0.029, 0.677) #, fit_C)
fit_Co = energy(x_fit, 0.0099, 0.128) + 1.5
fit_Ni = energy(x_fit, 0.0082, -0.09) + 1.3
plt.errorbar(x_data, y_data, yerr=y_err, fmt='bo', label='Measured spin waves for Mn')
plt.plot(x_fit, fit_Mn, 'y-', label="Mn with spin 5/2")  # , J_prime={fit_C:.2f}')
plt.plot(x_fit, fit_Ni, "g-", label="Ni with spin 1")
plt.plot(x_fit, fit_Co, "r-", label="Co with spin 1/2")
plt.xlim((0,1))
plt.xlabel("(Qh,Qh,0) (r.l.u.)")
plt.ylim((0, 2.5))
plt.ylabel("E(meV)")
plt.legend()
plt.savefig("6_9_2023_NI12/spin_polarized_state/srovnani_spin_waves.pdf")
plt.show()




