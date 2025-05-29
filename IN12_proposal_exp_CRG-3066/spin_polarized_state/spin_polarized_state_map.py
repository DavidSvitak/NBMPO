from ufit import *
import numpy as np
import matplotlib.pyplot as plt
from ufit.plotting import mapping
from scipy.optimize import curve_fit

def energy(k_x, J, B_star):
    S = 5/2
    # - 6*S*J_prime
    return 2*S*J*(np.cos(2*np.pi*k_x) + 2*np.cos(np.pi*k_x)*np.cos(np.pi*k_x + 2*np.pi*k_x)) + B_star
    # B_star = spin * landau factor * moment of Mn * field = 10 T;  

set_datatemplate("IN12_proposal_exp_CRG-3066/rawdata/075%03d")
#246, 247, 250-257, 259-263


x_data = []
y_data = []
y_err = []
numbers = [253, 254, 255, 256, 257, 259, 263, 260, 261, 262]

for num in numbers:
    data = read_data(num, "EN", "CNTS")
    model = Background() + Gauss("p1", pos=limited(0.3,1.2, 0.5), ampl=1500, fwhm=limited(0,0.5,0.1)) + \
        Gauss("p2", pos=0, ampl=26166, fwhm=0.082882)
    fixed(model.params[4])
    fixed(model.params[5])
    fixed(model.params[6])
    model.fit(data)
    x = data["QH"]
    y = model.params[1].value
    yerr = model.params[3].value/3
    x_data = np.append(x_data, [x], axis=0)
    y_data = np.append(y_data, [y], axis=0)
    y_err = np.append(y_err, [yerr], axis=0)
    print("Done")

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

data = read_numors("246-247, 250-257,259-263", 0)
mapping("QH", "EN", data, minmax=[0, 1500], interpolate=200, label= "Intensity (arb. unit)")
plt.errorbar(x_data, y_data, yerr=y_err, fmt='ro', label='Positions of Gaussian maxima')
plt.plot(x_fit, fit_y, 'r-', label="Magnon dispersion")  # , J_prime={fit_C:.2f}')
plt.xlabel("(Qh,Qh,0) (r.l.u.)")
plt.ylabel("E(meV)")
plt.ylim((0, 1))
plt.xlim((0.3, 0.6))
plt.legend()
plt.savefig("IN12_proposal_exp_CRG-3066/spin_polarized_state/spin_polarized_state_srovnani.png")
plt.show()
