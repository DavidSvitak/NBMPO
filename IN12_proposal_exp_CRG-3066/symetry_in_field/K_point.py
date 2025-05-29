from ufit import *
import numpy as np
import matplotlib.pyplot as plt
from ufit.plotting import mapping
# 238, 256, 265, 268, 271, 274, 280, 289, 293, 297, 313, 332, 334, 338, 340

set_datatemplate('IN12_proposal_exp_CRG-3066/rawdata/075%03d')
#model = Background() + Gauss("elastic", pos=0, ampl=250000, fwhm=0.02) + Gauss("peak1", pos=)
data = read_numors("238, 256, 265, 268, 271, 274, 280, 289, 293, 297, 313, 332, 334, 338, 340", 0)
data.name = "K point"
mapping("MAG", "EN", data, mode=0, title=f'{data.name}',log = True)
plt.savefig("IN12_proposal_exp_CRG-3066/symetry_in_field/K_point.png")
plt.show()
