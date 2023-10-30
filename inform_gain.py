# My Utility : 

import numpy  as np   

# estimation of information
def inform_estimate(X,N,m):
    # Extraer las etiquetas de clase
    clases = X[:, 41]

    # Calcular el número de muestras para cada clase
    di = [np.sum(clases == i) for i in m]

    # Inicializar la variable para almacenar la información estimada de la clase
    info_estimada_clase = 0

    # Calcular la información estimada de la clase
    for i in range(len(m)):
        pi = di[i] / N
        info_estimada_clase += pi * np.log2(pi)                
    
    return -info_estimada_clase

# Entropy of the variables  
def entropy_xy(X,N,m,I):
    B = int(np.sqrt(N))
        
    # Extraer las etiquetas de clase
    clases = X[:, 41]

    distribucion_conjunta = np.zeros((len(m), B))

    for i in range(len(m)):
        for j in range(B):
            # Calcula el número de muestras de la i-ésima clase en el j-ésimo bin
            d_ij = np.sum((clases == m[i]) & (X[:, columna_de_variable_X] == j))
            distribucion_conjunta[i, j] = d_ij 
    return()



#-----------------------------------------------------------------------
