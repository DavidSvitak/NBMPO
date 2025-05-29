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

set_datatemplate('IN12_proposal_exp_CRG-3066/rawdata/075%03d')
data = read_data(168, 'A3P',"CNTS")
model = Background() + Gauss('peak1', pos=31, ampl=13000, fwhm=3) + Gauss('peak2', pos=29, ampl=4000,fwhm=1) + Gauss('peak3', pos=27, ampl=1000, fwhm=1)
data.name = 'data'
result = model.fit(data)
peak1 = integrate.quad(lambda x: G(x, result.paramvalues['peak1_pos'], result.paramvalues['peak1_ampl'], result.paramvalues['peak1_fwhm']),result.paramvalues['peak1_pos']-50, result.paramvalues['peak1_pos']+50 )
peak2 = integrate.quad(lambda x: G(x, result.paramvalues['peak2_pos'], result.paramvalues['peak2_ampl'], result.paramvalues['peak2_fwhm']),result.paramvalues['peak2_pos']-50, result.paramvalues['peak2_pos']+50 )
peak3 = integrate.quad(lambda x: G(x, result.paramvalues['peak3_pos'], result.paramvalues['peak3_ampl'], result.paramvalues['peak3_fwhm']),result.paramvalues['peak3_pos']-50, result.paramvalues['peak3_pos']+50 )

intensity = peak1[0] + peak2[0] + peak3[0] 
peak1 = peak1[0]/intensity*100
peak2 = peak2[0]/intensity*100
peak3 = peak3[0]/intensity*100

with open("IN12_proposal_exp_CRG-3066/ALSA_coaligment/(002)_result.txt", "a") as txt:
    txt.write(f'Intensity of peak1 = {round(peak1,2)}% and FWHM = {round(result.paramvalues["peak1_fwhm"],2)}\n')
    txt.write(f'Intensity of peak2 = {round(peak2,2)}% and FWHM = {result.paramvalues["peak2_fwhm"]}\n')
    txt.write(f'Intensity of peak3 = {round(peak3,2)}% and FWHM = {result.paramvalues["peak3_fwhm"]}\n')

fig = plt.figure(figsize=(10, 10), dpi=100)    
ax = fig.add_subplot(1,1,1)
ax.yaxis.grid(color='white')
ax.xaxis.grid(color='white')
model.plot(data)
model.plot_components(data)
result.printout()

data.plot(lines=False)
plt.legend(fontsize=20)
plt.xlabel(r'$ \Theta$ $(^{\circ}) $', fontsize=20)
plt.title('')
plt.ylabel('Intensity (arb. unit)', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.savefig("IN12_proposal_exp_CRG-3066/ALSA_coaligment/(002).png", dpi=600)
plt.show()
