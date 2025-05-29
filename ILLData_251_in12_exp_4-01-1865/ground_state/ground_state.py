from ufit import *
from ufit.plotting import mapping
import matplotlib.pyplot as plt

set_datatemplate('rawdata/079%03d')
data = read_numors("197-209", 0)
data.name = ""
mapping("QH", "EN", data, mode=0, title=f'{data.name}',minmax=[0,2500])
plt.savefig("ground_state/ground_state.png")
plt.show()