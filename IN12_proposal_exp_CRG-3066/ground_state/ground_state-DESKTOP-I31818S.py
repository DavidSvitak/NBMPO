from ufit import *
import numpy as np
import matplotlib.pyplot as plt
from ufit.plotting import mapping

set_datatemplate('IN12_proposal_exp_CRG-3066/rawdata/075%03d')
# from 223 to 234 and 311
# 232 with two peaks 
#data = read_numors("")

"""
model = Background() + Gauss("elastic_line", pos=0, ampl=20000, fwhm=0.045) + Gauss("peak1", pos=0.15, ampl=1500, fwhm=0.11)
data = read_data(234, "EN")
model.plot_components(data)
fit = model.fit(data)
model.plot(data)
fit.printout()
data.plot()
"""

data = read_numors("222-228,230-235, 237, 311", 0)
data.name = "Spin waves in ground state"
mapping("QH", "EN", data, mode=0, title=f'{data.name}', log=True)
plt.ylim((0,0.5))
plt.xlabel("Q = (Qh, Qh, 0.18)")
plt.ylabel("E(meV)")
plt.savefig("IN12_proposal_exp_CRG-3066/ground_state/ground_state.png")

plt.show()


