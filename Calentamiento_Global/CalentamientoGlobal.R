

library(gdata)
library(ggplot2)
library(reshape2)
library(plyr)
library(dplyr)

pkgs <- c('reshape2', 'plyr', 'ggplot2', 'dplyr', 'data.table', 'Lahman')


#Links
#Bogota_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_13_0/station.txt"
#Cali_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_13_0/station.txt"
#Bucaramanga_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_13_0/station.txt"
#Barranquilla_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_13_0/station.txt"
#Ipiales_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_13_0/station.txt"

#Dado que los links son dinamicos, se decide descargar los archivos 1 sola
#vez y llamarlos directamente desde su ubicacion en en el disco
#Los archivos existentes son:
#Bogota.txt
#Barranquilla.txt
#Bucarmanga.txt
#Cali.txt
#Ipiales.txt


#Cargar datos crudos desde el disco
#Datos de Bogotá
Bogota <- read.table(
  file = "Bogota.txt",
  header = TRUE,
  )
n <- names(Bogota)[1:13] #Seleccionar los nombres de las columnas a usar
Bogota <- Bogota[c(n)] #Eliminar las columnas que no se usan
Bogota_tidy <- melt(
  data = Bogota,
  id = "YEAR",
  variable.name = "Month",
  value.name = "Temperature"
  )
Bogota_tidy$Day = 1
Bogota_tidy$City = "Bogota"
Bogota_tidy <- Bogota_tidy[c("YEAR","Month","Day","City","Temperature")]
#Cali_rdata <- read.table(Cali_url)
#Bucaramanga_rdata <- read.table(Bucaramanga_url)
#Barranquilla_rdata <- read.table(Barranquilla_url)
#Ipiales_rdata <- read.table(Ipiales_url)


#----
#Procesar datos
#Extraer los datos numericos de cada dataframe de datos crudos y organizarlos
#en un Ãºnico dataframe. Cada fila como esta en los datos crudos va a ser una 
#observacion en los datos limpios. Agrego variable 'Ciudad' con el nombre de
#la ciudad que corresponde a cada observacion de los datos.