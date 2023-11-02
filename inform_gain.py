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
    # Obtenemos los valores unicos del atributo
    unique_values, value_counts = np.unique(X_column, return_counts=True)

    # Cortamos los valores hasta B
    B = int(np.sqrt(len(X_column)))
    unique_values = unique_values[:B]
    value_counts = value_counts[:B]

    # Calculamos la "entropia"
    E = 0 
    for value in unique_values:
        subset_indices = np.where(X_column == value)
        subset_data = Y[subset_indices]
        E += (len(subset_data) / len(Y)) * inform_estimate(subset_data)
    return E

#-----------------------------------------------------------------------
