from ufit import *
from ufit.plotting import mapping
import matplotlib.pyplot as plt
set_datatemplate('ILLData_251_in12_exp_4-01-1865_rawdata/rawdata/079%03d')
data = read_numors("197-209", 0)
data.name = ""
mapping("QH", "EN", data, mode=0, title=f'{data.name}',minmax=[0,2500])

plt.show()