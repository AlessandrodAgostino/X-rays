import numpy as np
import matplotlib.pylab as plt
from os.path import join as pj

Ladder_img = np.fromfile(pj('Aquisition 4','ladder_120kV_micoA4100_16average_10frate.sdt'), dtype='uint16', sep="")
Ladder_img = np.reshape(Ladder_img, (1920, 1536))

I0_img = np.fromfile(pj('Aquisition 4','I0_120kV_micoA4100_16average_10frate.sdt'), dtype='uint16', sep="")
I0_img = np.reshape(I0_img, (1920, 1536))

dark = np.fromfile('dark.sdt', dtype='uint16', sep="")
dark = np.reshape(dark, (1920, 1536))

#Should increase the contrast!
plt.imshow((Ladder_img - dark)/I0_img)
