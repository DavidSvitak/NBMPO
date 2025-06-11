import numpy as np
import matplotlib.pyplot as plt
from ufit.lab import *
from ufit.plotting import mapping
import pandas as pd
from scipy.optimize import curve_fit







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
fit_y_Mn = energy(x_fit, fit_A, fit_B) #, fit_C)
fit_y_Co = energy(x_fit, 0.076, 1.451/11.4/10/3.5) #, fit_C)
plt.errorbar(x_data, y_data, yerr=y_err, fmt='o', label='data')
plt.plot(x_fit, fit_y_Mn, 'b-')  # , J_prime={fit_C:.2f}')
plt.plot(x_fit, fit_y_Co, 'r-')  # , J_prime={fit_C:.2f}')
plt.legend()
plt.show()