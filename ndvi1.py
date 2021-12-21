import rasterio
import numpy
import matplotlib.pyplot as plt

with rasterio.open('cropped.TIF') as src:
    band_red = src.read(1)

with rasterio.open('cropped1.TIF') as src:
    band_nir = src.read(1)

numpy.seterr(divide='ignore', invalid='ignore')

ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
print(ndvi)

kwargs = src.meta
kwargs.update(
    dtype=rasterio.float32,
    count=1)

with rasterio.open('NDVI.TIF', 'w', **kwargs) as dst:
    dst.write_band(1, ndvi.astype(rasterio.float32))

plt.imsave("NDVI-cmap.png", ndvi, cmap=plt.cm.PuBu)