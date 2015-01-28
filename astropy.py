import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.utils.data import download_file
from astropy.io import fits

image_list = [ download_file('http://www.mistisoftware.com/astronomy/fits/'+n+'m_L.FIT', cache=True ) \
                for n in ['m27_050711_6i30', 'ngc7293_050906_8i40']]

image_concat = []
for image in image_list:
    plt.figure()
    hdu_list = fits.open(image)
    hdu_list.info()

    image_data = hdu_list[0].data
    hdu_list.close()
    plt.imshow(image_data,cmap='jet')
    plt.draw()
    image_concat.append(fits.getdata(image))
plt.figure()

final_image = np.sum(image_concat, axis=0)

plt.imshow(final_image, cmap='jet')
plt.colorbar()
plt.draw()

plt.show()

outfile = 'concat.fits'
hdu = fits.PrimaryHDU(final_image)
hdu.writeto(outfile, clobber=True)