from ufit import *
import numpy as np
import matplotlib.pyplot as plt
from ufit.plotting import mapping

set_datatemplate('IN12_proposal_exp_CRG-3066/rawdata/075%03d')

# 345, 346, 347, 349 - 359
data = read_numors("345, 346, 347, 349-359", 0)
data.name = "600 mK 3T"
mapping("QH", "EN", data, mode=0, title=f'{data.name}', minmax=[0, 2000])
plt.savefig("IN12_proposal_exp_CRG-3066/600mK3T/600mK3T.png")

plt.show()





