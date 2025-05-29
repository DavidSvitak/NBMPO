from ufit import *
import numpy as np
import matplotlib.pyplot as plt
from ufit.plotting import mapping
from data_preparation import prepare
set_datatemplate('IN12_proposal_exp_CRG-3066/rawdata/075%03d')
# 333, 331, 312, 276, 273, 270, 267, 246, 235, 246, 247, 264, 267, 270, 273, 276, 285, 298, 294, 290





"""
combine:
264+247+246 gamma 10T 
265+256 K point 10T
267+290 gamma point 9T
268+289 K point 9T
293+271 K point 8T
270+294 gamma point 8T
273+298 gamma point 7T
297+274 K point 7T
331+341 gamma point 5T
276+285 gamma point 6T
"""
data = read_data(265, "EN")
data.plot()
model = Background() + Gauss("elastic", pos=0, ampl=250000, fwhm=0.02) + Gauss("peak1", pos=0.8, ampl=3000, fwhm=0.05)

for num in [333, 331, 312, 276, 273, 270, 267, 246, 235, 246, 247, 264, 267, 270, 273, 276, 285, 298, 294, 290]:
    fig = plt.figure()
    data = read_data(num, "EN")
    data.plot()

data = read_numors("341, 339, 337, 333, 331, 312, 276, 273, 270, 267, 246, 235, 246, 247, 264, 267, 270, 273, 276, 285, 298, 294, 290", 0)
data.name = "Gamma point"
mapping("MAG", "EN", data, mode=0, title=f'{data.name}',log = True)
plt.savefig("IN12_proposal_exp_CRG-3066/symetry_in_field/gamma_point.png")

plt.show()




