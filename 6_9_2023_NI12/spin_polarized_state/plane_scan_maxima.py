import numpy as np
import matplotlib.pyplot as plt
from ufit.lab import *
from ufit import gui
from ufit.plotting import mapping
set_datatemplate('6_9_2023_NI12/spin_polarized_state/070%03d')
x_data = []
y_data = []
y_err = []
numbers = [215, 216, 217, 222, 223, 224, 225, 226, 227, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]
"""
for num in numbers:
    data = read_data(num, "EN", "CNTS")
    model = Background() + Gauss("p1", pos=limited(0.3,0.9, 0.5), ampl=limited(0,300,200), fwhm=limited(0,0.5,0.1)) + \
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

model = Background() + Gauss("p1", pos=limited(1, 1.2, 1), ampl=limited(700, 1000, 900), fwhm=limited(0, 0.5, 0.1))
data = read_data(261, "EN", "CNTS")
model.fit(data)
x = data["QH"]
y = model.params[1].value
x_data = np.append(x_data, [x], axis=0)
y_data = np.append(y_data, [y], axis=0)
print("Done")
"""
data = read_numors('215,216,217,222-227, 243-256, 261', 0)
mapping('QH', 'EN', data, mode=0, title="", minmax=[0, 1000], label="Intensity (arb. unit)")
plt.xlabel('(Qh,Qh,0) (r.l.u.)')
plt.ylabel('E(meV)')
plt.xlim((0.3, 0.6))
plt.ylim((0, 1))
"""
f = open('6_9_2023_NI12/spin_polarized_state/plot_data.txt', 'w')
for d in zip(x_data, y_data, y_err):
    f.write(f'{round(d[0],4)}    {round(d[1],4)}    {round(d[2], 4)}\n')
f.close()
plt.plot(x_data, y_data, 'bo')
"""
plt.show()


