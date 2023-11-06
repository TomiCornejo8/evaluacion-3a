# My Utility : 

import numpy  as np   

# estimation of information
def inform_estimate(data):
    # Obtenemos las clases unicas m y la cantidad que aparecen estas clases 
    m, di = np.unique(data, return_counts=True)

    # Sacar probabilidades de las clases
    pi = di/len(data)         
    
    return -np.sum(pi*np.log2(pi))

# Entropy of the variables  
def entropy_xy(X_column,Y):    
    N = len(X_column)
    B = int(np.sqrt(N))

    # Calcula la resolución
    resolucion = (np.max(X_column) - np.min(X_column)) / B

    # Calcula los límites de X_column
    limites = (np.arange(B) * resolucion) + np.min(X_column)

    # Calcula los intervalos
    intervalos = np.digitize(X_column, limites)

    # Obtenemos los valores unicos del atributo
    unique_values = np.unique(intervalos)

    # Calculamos la "entropia"
    E = 0 
    for value in unique_values:
        subset_indices = np.where(intervalos == value)[0]
        subset_data = Y[subset_indices]
        E += (len(subset_data) / len(Y)) * inform_estimate(subset_data)
    return E

#-----------------------------------------------------------------------
