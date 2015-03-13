

library(gdata)
library(ggplot2)
library(MODISTools)

#Links
Bogota_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_13_0/station.txt"
Cali_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_13_0/station.txt"
Bucaramanga_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_13_0/station.txt"
Barranquilla_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_13_0/station.txt"
Ipiales_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_13_0/station.txt"

#Cargar datos crudos
Bogota_rdata <- read.table(Bogota_url)
Cali_rdata <- read.table(Cali_url)
Bucaramanga_rdata <- read.table(Bucaramanga_url)
Barranquilla_rdata <- read.table(Barranquilla_url)
Ipiales_rdata <- read.table(Ipiales_url)

#----
#Procesar datos
#Extraer los datos numericos de cada dataframe de datos crudos y organizarlos
#en un único dataframe. Cada fila como esta en los datos crudos va a ser una 
#observacion en los datos limpios. Agrego variable 'Ciudad' con el nombre de
#la ciudad que corresponde a cada observacion de los datos.