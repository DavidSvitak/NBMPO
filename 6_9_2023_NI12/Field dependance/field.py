import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from ufit.lab import *
from ufit.plotting import mapping

set_datatemplate('6_9_2023_NI12/Field dependance/070%03d')
data = read_data(133, "MAG")
data.name = ''
data.plot()
plt.title('Field dependance of magnetic bragg peak at 50mK')
plt.xlim((0, 7))
plt.ylim((0, 120000))
plt.xlabel("B(T)")
plt.ylabel("Int. (arb. unit)")
plt.show()
