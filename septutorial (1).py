#!/usr/bin/env python
# coding: utf-8

# ## final project - sep tutorial (4 pngs)

# 1) Get astropy and install it on your system (pip install astropy).
# 
# 2) Get sep and install it on your system (pip install sep).
# 
# 3) Follow the tutorial found at https://sep.readthedocs.io/en/stable/tutorial.htmlLinks to an external site., but use the astropy fits routines instead of fitsio. Create a notebook that performs the tutorial and comment it using Markdown to explain what it’s doing. Note that the fits image used in the tutorial can be acquired via the sep GitHub account.
# 
# 4) Augment the tutorial to save each of the four figures to PNG files.

# In[7]:


import numpy as np
import sep
from astropy.io import fits
import matplotlib.pyplot as plt

# Load FITS image
from astropy.io import fits

data = fits.getdata("image.fits").astype(float)
data = np.ascontiguousarray(data)

data.shape


# In[10]:


bkg = sep.Background(data)
data_sub = data - bkg

objects = sep.extract(data_sub, thresh=1.5 * bkg.globalrms)
print(len(objects))


# In[11]:


plt.imshow(data, cmap='gray', origin='lower')
plt.title("Original Image")
plt.savefig("tutorial_image.png")
plt.show()


# In[12]:


plt.imshow(bkg.back(), cmap='gray', origin='lower')
plt.title("Background")
plt.savefig("tutorial_background.png")
plt.show()


# In[13]:


plt.imshow(bkg.rms(), cmap='magma', origin='lower')
plt.title("Background RMS")
plt.savefig("tutorial_rms.png")
plt.show()


# In[14]:


segmap = np.zeros_like(data, dtype=int)
for i, obj in enumerate(objects):
    segmap[obj['ymin']:obj['ymax'], obj['xmin']:obj['xmax']] = i+1

plt.imshow(segmap, origin='lower')
plt.title("Segmentation Map")
plt.savefig("tutorial_segmap.png")
plt.show()


# In[16]:


# available fields
objects.dtype.names


# In[17]:


flux, fluxerr, flag = sep.sum_circle(data_sub, objects['x'], objects['y'],
                                     3.0, err=bkg.globalrms, gain=1.0)


# In[18]:


# show the first 10 objects results:
for i in range(10):
    print("object {:d}: flux = {:f} +/- {:f}".format(i, flux[i], fluxerr[i]))

