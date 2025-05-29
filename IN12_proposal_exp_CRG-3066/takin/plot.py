import matplotlib.pyplot as plt
from ufit import *
from ufit.plotting import mapping

set_datatemplate("IN12_proposal_exp_CRG-3066/takin/1%03d.txt")
data = read_numors("0-99", 0)
k = mapping("Qh", "En", data, mode=0, title="", minmax=[0, 0.4], dots=False, label=r"S(Q,$\omega$)")
plt.ylabel("E(meV)")
plt.ylim((0,1))
plt.xlabel("(Qh, Qh, 0) (r.l.u.)")

plt.savefig("IN12_proposal_exp_CRG-3066/takin/limited_spectrum.png", dpi=600)
plt.show()
