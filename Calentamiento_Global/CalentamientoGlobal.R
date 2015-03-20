
library(ggplot2)
library(reshape2)
library(plyr)
library(dplyr)
library(lubridate)

setwd("./")
#Links
#Bogota_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_13_0/station.txt"
#Cali_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_13_0/station.txt"
#Bucaramanga_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_13_0/station.txt"
#Barranquilla_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_13_0/station.txt"
#Ipiales_url <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_13_0/station.txt"

#Dado que los links son dinamicos, se decide descargar los archivos una sola
#vez y llamarlos directamente desde su ubicacion en en el disco
#Los archivos existentes son:
#Bogota.txt
#Barranquilla.txt
#Bucarmanga.txt
#Cali.txt
#Ipiales.txt

Ciudades <- c('Bogota', 'Barranquilla', 'Bucaramanga', 'Cali', 'Ipiales')
a = c() #Serie vacia
Data = data.frame(a,a,a) # DataFrame vacio. En este data frame se van a guardar los datos tidy
for(C in Ciudades) { 
  
  #Cargar datos
  Data_raw <- read.table(
    file = paste(C,".txt",sep=""),
    header = TRUE)
  
  n <- names(Data_raw)[1:13] #Seleccionar los nombres de las columnas a usar
  Data_raw <- Data_raw[c(n)] #Guardar solo las 13 primeras columnas
  
  # Tidy data. Hacer melt para generar datos tidy
  Data_tidy <- melt(
    data = Data_raw,
    id = "YEAR",
    variable.name = "Month",
    value.name = "Temperature"
  )
  
  #Agregar columnas de Ciudad y dia
  Data_tidy$Day = 1
  Data_tidy$City = C
  
  Data = rbind(Data,Data_tidy) #Agrupar todos los datos en un unico DataFrame
}

# Ordenar las columnas
Data <- Data[c("YEAR","Month","Day","City","Temperature")]
names(Data) <- c('anno','mes','fecha','ciudad','temperatura')

#Reemplazar datos de temperatura = 999.9 con NaN
Data$temperatura[Data$temperatura == 999.9] <- NaN
# Se cambian los niveles del mes para que no haya problema al usar dmy{lubridate}
levels(Data$mes) <- c(1,2,3,4,5,6,7,8,9,10,11,12)
Data$fecha <- dmy(paste(1,Data$mes,Data$anno,sep="-"))
