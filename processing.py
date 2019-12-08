import numpy as np
import matplotlib.pylab as plt
from os.path import join as pj
import seaborn as sns

Ladder_img = np.fromfile(pj('Aquisition 4','ladder_120kV_micoA4100_16average_10frate.sdt'), dtype='uint16', sep="")
Ladder_img = np.reshape(Ladder_img, (1920, 1536))

I0_img = np.fromfile(pj('Aquisition 4','I0_120kV_micoA4100_16average_10frate.sdt'), dtype='uint16', sep="")
I0_img = np.reshape(I0_img, (1920, 1536))

dark = np.fromfile('dark.sdt', dtype='uint16', sep="")
dark = np.reshape(dark, (1920, 1536))

#Should increase the contrast!
plt.imshow((Ladder_img - dark)/I0_img)


#Measuring average graylevel
ampere = np.linspace(0,6, 7, dtype=np.int16)
ampere = ampere*5 + 10
print(ampere)

dark = np.fromfile('dark.sdt', dtype='uint16', sep="")
dark = np.reshape(dark, (1920, 1536))

average_gl_16frame = np.zeros(7)
for n,amp in enumerate(ampere):
  filename= f'microA{amp}00_average16.sdt'
  img = np.fromfile(pj('Aquisition 1',filename), dtype='uint16', sep="")
  img = np.reshape(img, (1920, 1536))
  img = img -dark
  average_gl_16frame[n]= np.average(img[200:800, 200:800])

average_gl_1frame = np.zeros(7)
for n,amp in enumerate(ampere):
  filename= f'microA{amp}00.sdt'
  img = np.fromfile(pj('Aquisition 1',filename), dtype='uint16', sep="")
  img = np.reshape(img, (1920, 1536))
  img = img -dark
  average_gl_1frame[n]= np.average(img[200:800, 200:800])

plt.scatter(ampere, average_gl_16frame)
plt.scatter(ampere, average_gl_1frame)
