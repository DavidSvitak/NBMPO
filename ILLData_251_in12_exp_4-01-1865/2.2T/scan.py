from ufit import *
from ufit.plotting import mapping
import matplotlib.pyplot as plt


set_datatemplate('rawdata/079%03d')
data = read_numors("213-215, 217-222, 232, 334-243", 0)
data.name = ""
mapping("QH", "EN", data, mode=0, title=f'{data.name}', minmax=[0,1000])
plt.savefig("2.2T/22T.png")
plt.show()