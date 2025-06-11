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
data = read_data(52, 'A3P',"CNTS")
model = Background() + Gauss('peak1', pos=135, ampl=400, fwhm=1) + Gauss('peak2', pos=137, ampl=500,fwhm=1.1176) + Gauss('peak3', pos=139, ampl=900, fwhm=1) + Gauss('peak4',pos=141,ampl=1100,fwhm=1) 
data.name = 'data'
result = model.fit(data)
peak1 = integrate.quad(lambda x: G(x, result.paramvalues['peak1_pos'], result.paramvalues['peak1_ampl'], result.paramvalues['peak1_fwhm']),result.paramvalues['peak1_pos']-50, result.paramvalues['peak1_pos']+50 )
peak2 = integrate.quad(lambda x: G(x, result.paramvalues['peak2_pos'], result.paramvalues['peak2_ampl'], result.paramvalues['peak2_fwhm']),result.paramvalues['peak2_pos']-50, result.paramvalues['peak2_pos']+50 )
peak3 = integrate.quad(lambda x: G(x, result.paramvalues['peak3_pos'], result.paramvalues['peak3_ampl'], result.paramvalues['peak3_fwhm']),result.paramvalues['peak3_pos']-50, result.paramvalues['peak3_pos']+50 )
peak4 = integrate.quad(lambda x: G(x, result.paramvalues['peak4_pos'], result.paramvalues['peak4_ampl'], result.paramvalues['peak4_fwhm']),result.paramvalues['peak4_pos']-50, result.paramvalues['peak4_pos']+50 )
intensity = peak1[0] + peak2[0] + peak3[0] + peak4[0] 
peak1 = peak1[0]/intensity*100
peak2 = peak2[0]/intensity*100
peak3 = peak3[0]/intensity*100
peak4 = peak4[0]/intensity*100
print(f'Intensity of peak1 = {round(peak1,2)}% and FWHM = {round(result.paramvalues["peak1_fwhm"],2)}')
print(f'Intensity of peak2 = {round(peak2,2)}% and FWHM = {result.paramvalues["peak2_fwhm"]}')
print(f'Intensity of peak3 = {round(peak3,2)}% and FWHM = {result.paramvalues["peak3_fwhm"]}')
print(f'Intensity of peak4 = {round(peak4,2)}% and FWHM = {result.paramvalues["peak4_fwhm"]}')


weight1 = 0.38
weight2 = 0.35
weight3 = 0.33
weight4 = 0.33
weight5 = 0.33
weight6 = 0.32

weight = weight1 + weight2 + weight3 + weight4 + weight5 + weight6

weight1 = weight1/weight
weight2 = weight2/weight
weight3 = weight3/weight
weight4 = weight4/weight
weight5 = weight5/weight
weight6 = weight6/weight

print(weight1 + weight2)
print(weight3  + weight4)
print(weight5)
print(weight6)
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
plt.ylabel('Int (arb. unit)', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.savefig('6_9_2023_NI12/ALSA_coaligment/old_c_axis.png', dpi=600)
plt.show()


