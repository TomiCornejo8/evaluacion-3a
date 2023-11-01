# My Utility : 

import numpy  as np   

# normalization of the data
def norm_data(X):
    # Definimos los valores de a y b
    a = 0.01
    b = 0.99

    # Calcula los valores mínimos y máximos
    x_min = X.min(axis=0)
    x_max = X.max(axis=0)

    x_max[x_max == x_min] += 1e-20 # Para evitar divisiones con 0

    # Realiza la normalización
    X = ((X - x_min) / (x_max - x_min)) * (b - a) + a
        
    return X

# SVD of the data
def svd_data():
    ...    
    return()



#-----------------------------------------------------------------------
