# My Utility : 

import numpy  as np   

# normalization of the data
def norm_data(X):
    # Definimos los valores de a y b
    a = 0.01
    b = 0.99

    # Calcula los valores mínimos y máximos de las columnas 1 a 41
    x_min = X[:, 0:41].min(axis=0)
    x_max = X[:, 0:41].max(axis=0)

    x_max[x_max == x_min] += 1e-20 # Para evitar divisiones con 0

    # Realiza la normalización para las columnas 1 a 41
    X[:, 0:41] = ((X[:, 0:41] - x_min) / (x_max - x_min)) * (b - a) + a
        
    return X

# SVD of the data
def svd_data():
    ...    
    return()



#-----------------------------------------------------------------------
