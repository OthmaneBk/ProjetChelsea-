import pandas as pd

def collecte_data():
   data_path = 'data/gpsD1.csv'
   data_gps=pd.read_csv(data_path,encoding='latin-1',sep=';')
   return data_gps