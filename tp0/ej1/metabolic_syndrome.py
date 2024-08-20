import pandas as pd
import matplotlib.pyplot as plt

# Definimos una variable con el path
path_data = "data/Metabolic Syndrome.csv"

def main():
  # Leemos un archivo de texto separado por comas (csv) y lo instanciamos como un DataFrame
  data = pd.read_csv(path_data)
  return data

def data_resume():
  # Resumen general del DataFrame
  print('Info:')
  print(data.info())
  # Resumen estadístico de las variables numéricas
  print('Description:')
  print(data.describe())
  # Revisar la cantidad de valores nulos
  print('Null Data:')
  print(data.isnull().sum())

data = main()

data_resume()