import pandas as pd

def collecte_data():
   data_gps=pd.read_csv('D://Othmane//4eme//ChelaseProjet//GpsData//data//gpsD1.csv',encoding='latin-1',sep=';')
   return data_gps