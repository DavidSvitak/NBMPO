import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from ufit.lab import *
from ufit.plotting import mapping
 
set_datatemplate("IN12_proposal_exp_CRG-3066/rawdata/075%03d")
QH_data = read_data(222, "QH")
QL_data = read_data(221, "QL")

model_QH = Background() + Gauss("Propagation_vector", pos=0.333, ampl=17000, fwhm=0.02)
model_QL = Background() + Gauss("Propagation_vector", pos=0.18, ampl=17500, fwhm=1) 





QH_fit = model_QH.fit(QH_data)
QL_fit = model_QL.fit(QL_data)

QH_fit.printout()
QL_fit.printout()
QH_data.plot()
model_QH.plot(QH_data)
fig = plt.figure()
QL_data.plot()
model_QL.plot(QL_data)

plt.show()



