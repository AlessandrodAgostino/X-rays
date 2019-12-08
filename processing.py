import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

"""
Measuring average gray levels in the same ROI of different images took with
different current intensities.
Analysing always the same ROI for every image.
From every image the "dark" image has been subtracted (image took with x-ray
source tourned off).
The linear regression plot in drawn -> perfectly linear relation.
"""

#%%
#different ampere values -> filenames parsing
ampere = np.linspace(0,6, 7, dtype=np.int16)
ampere = ampere*5 + 10
print(ampere)

#loading the dark image
dark = np.fromfile('dark.sdt', dtype='uint16', sep="")
dark = np.reshape(dark, (1920, 1536))

#loading and analysing the same ROI on every 16 average frame image
average_gl_16frame = np.zeros(7)
for n,amp in enumerate(ampere):
  filename= f'microA{amp}00_average16.sdt'
  img = np.fromfile(pj('Aquisition 1',filename), dtype='uint16', sep="")
  img = np.reshape(img, (1920, 1536))
  img = img -dark
  average_gl_16frame[n]= np.average(img[200:800, 200:800])

#loading and analysing the same ROI on every 1 frame image
average_gl_1frame = np.zeros(7)
for n,amp in enumerate(ampere):
  filename= f'microA{amp}00.sdt'
  img = np.fromfile(pj('Aquisition 1',filename), dtype='uint16', sep="")
  img = np.reshape(img, (1920, 1536))
  img = img -dark
  average_gl_1frame[n]= np.average(img[200:800, 200:800])

#%%
#Plotting the results
fig = plt.figure()
sns.regplot(ampere, average_gl_16frame)
# sns.regplot(ampere, average_gl_16frame) #superimposing perfectly
fig.suptitle('GL - Current', fontsize=20)
plt.xlabel('Current (mA)', fontsize=18)
plt.ylabel('Grey Level', fontsize=16)
fig.savefig('Results/GL_current_linreg.jpg')
