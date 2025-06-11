import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from ufit.lab import *
from ufit.plotting import mapping
import ufit.gui as g
import scipy.integrate as integrate

def G(x, pos, ampl, fwh):
    return ampl*np.exp(-(x-pos)**2/(2*(fwh/4.29)**2))


set_datatemplate('6_9_2023_NI12/ALSA_coaligment/070%03d')
data = read_data(50, 'A3P',"CNTS")
data.name = 'data'
model = Background() + Gauss('peak1', pos=9.3593, ampl=36352, fwhm=4.0624) + Gauss('peak3', pos=5.0608, ampl=4093.5,fwhm=1.1176) + Gauss('peak4', pos=14.285, ampl=4759.4, fwhm=2.2144) + Gauss('peak2',pos=3.5194,ampl=2405.5,fwhm=2.7384) + Gauss('peak5',pos=16.805,ampl=2859.8,fwhm=2.0161)
result = model.fit(data)
peak1 = integrate.quad(lambda x: G(x, result.paramvalues['peak1_pos'], result.paramvalues['peak1_ampl'], result.paramvalues['peak1_fwhm']), -np.inf, np.inf)
peak2 = integrate.quad(lambda x: G(x, result.paramvalues['peak2_pos'], result.paramvalues['peak2_ampl'], result.paramvalues['peak2_fwhm']),-np.inf, np.inf)
peak3 = integrate.quad(lambda x: G(x, result.paramvalues['peak3_pos'], result.paramvalues['peak3_ampl'], result.paramvalues['peak3_fwhm']),-np.inf, np.inf)
peak4 = integrate.quad(lambda x: G(x, result.paramvalues['peak4_pos'], result.paramvalues['peak4_ampl'], result.paramvalues['peak4_fwhm']),-np.inf, np.inf)
peak5 = integrate.quad(lambda x: G(x, result.paramvalues['peak5_pos'], result.paramvalues['peak5_ampl'], result.paramvalues['peak5_fwhm']),-np.inf, np.inf)
intensity = peak1[0] + peak2[0] + peak3[0] + peak4[0] + peak5[0]
peak1 = peak1[0]/intensity*100
peak2 = peak2[0]/intensity*100
peak3 = peak3[0]/intensity*100
peak4 = peak4[0]/intensity*100
peak5 = peak5[0]/intensity*100
print(f'Intensity of peak1 = {round(peak1,2)}% and FWHM = {result.paramvalues["peak1_fwhm"]}')
print(f'Intensity of peak2 = {round(peak2,2)}% and FWHM = {result.paramvalues["peak2_fwhm"]}')
print(f'Intensity of peak3 = {round(peak3,2)}% and FWHM = {result.paramvalues["peak3_fwhm"]}')
print(f'Intensity of peak4 = {round(peak4,2)}% and FWHM = {result.paramvalues["peak4_fwhm"]}')
print(f'Intensity of peak5 = {round(peak5,2)}% and FWHM = {result.paramvalues["peak5_fwhm"]}')
result.printout()
fig = plt.figure(figsize=(10, 10), dpi=100)    
ax = fig.add_subplot(1,1,1)
ax.yaxis.grid(color='white')
ax.xaxis.grid(color='white')
model.plot(data)
model.plot_components(data)
data.plot()

plt.title('')
plt.legend(fontsize=20)
plt.ylabel('Int (arb. unit)', fontsize=20)
plt.xlim((-2,21))
plt.xlabel(r'$ \Psi$ $(^{\circ}) $',fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.savefig('6_9_2023_NI12/ALSA_coaligment/old_ab_axis.png', dpi=600)
plt.show()

