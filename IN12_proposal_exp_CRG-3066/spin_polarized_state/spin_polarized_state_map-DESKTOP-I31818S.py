from ufit import *
import numpy as np
import matplotlib.pyplot as plt
from ufit.plotting import mapping


set_datatemplate("IN12_proposal_exp_CRG-3066/rawdata/075%03d")
#246, 247, 250-257, 259-263
data = read_numors("246-247, 250-257,259-263, 330", 0)
data.name = "Spin polarized state B = 10 T"
mapping("QH", "EN", data, mode=0, title=f'{data.name}', log=True)
plt.xlabel("(Qh, Qh, 0.18)")
plt.ylabel("E(meV)")
plt.ylim((0, 1.5))
plt.savefig("IN12_proposal_exp_CRG-3066/spin_polarized_state/spin_polarized_state_extended.png")
plt.show()
