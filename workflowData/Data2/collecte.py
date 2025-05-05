import pandas as pd

def collecte_data():
   data_path = 'data/BioPlayer.csv'
   data_gps=pd.read_csv(data_path,encoding='latin-1',sep=';')
   return data_gps