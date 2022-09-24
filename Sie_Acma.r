library(sp)
library(raster)
r <- raster("C:/Users/power/Downloads/imagen1.tif")
bandas<-nbands(r)
re <- aggregate(r,fact=2)
writeRaster(re,filename="NuevoRaster.tif", format="GTiff",bands=bandas,overwrite=TRUE)
for (xx in 1:bandas){r[[xx]] <- raster("C:/Users/power/Downloads/imagen1.tif") re[[xx]] <- aggregate(r,fact=2)
writeRaster(re[[xx]],filename="NuevoRaster.tif", format="GTiff",overwrite=TRUE)}

