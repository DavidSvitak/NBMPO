from ufit import *
import numpy as np
import matplotlib.pyplot as plt
from ufit.plotting import mapping

set_datatemplate('IN12_proposal_exp_CRG-3066/rawdata/075%03d')
# 312-315, 318-329
data = read_numors("312-313,315,316,318-329", 0)
data.name = "Scan at T = 76 mK and B = 3T"
mapping("QH", "EN", data, mode=0, title=f'{data.name}',minmax=[0, 3000])
plt.ylim((0, 0.5))
plt.savefig("IN12_proposal_exp_CRG-3066/3T_scan/scan_3T.png")
plt.show()


