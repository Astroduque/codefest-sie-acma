# codefest-sie-acma
Procesamiento de imagenes Codefest
DESCRIPCIÓN DEL CÓDIGO
SIE_ACMA 
 
 
 
Programmed in Language R version 4.2.1 
Program Version: 01 
License: 
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details. 
 
Se abre consola del programa R 
Se instala la consola y el intérprete de R, se instalan las librerías; sp y raster con el comando Install.packages 


library(sp)      #instalar libreria
library(raster)  #instalar libreria
r <- raster("C:/Users/power/Downloads/imagen1.tif")   #r es el lenguaje de programación y se conecta con el comando raster las imágenes .tiff a la consola de R  
bandas<-nbands(r) #
re <- aggregate(r,fact=2)
writeRaster(re,filename="NuevoRaster.tif", format="GTiff",bands=bandas,overwrite=TRUE)
for (xx in 1:bandas){r[[xx]] <- raster("C:/Users/power/Downloads/imagen1.tif") re[[xx]] <- aggregate(r,fact=2)
writeRaster(re[[xx]],filename="NuevoRaster.tif", format="GTiff",overwrite=TRUE)}

Para cada raster, se busca conocer la cantidad de sus bandas, esto se realiza a través de la función nbands.
Luego, se procede a usar la función aggregate para comprimir el raster a través de un valor índice que permite realizar iteraciones con la calidad y el peso durante el proceso de compresión del raster, luego se escribe en un nuevo archivo raster, con la información del archivo que se comprimió previamente, se procede a insertar las bandas del raster comprimido en el raster a exportar. Finalmente se exporta como “Nuevoraster.tif”
 
