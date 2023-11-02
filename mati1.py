# My Utility : 

import numpy  as np   

# Estimación de información
def inform_estimate(data):
    # Obtenemos las clases únicas 'm' y la cantidad que aparecen estas clases 'di'
    m, di = np.unique(data, return_counts=True)

    # Sacar probabilidades de las clases
    pi = di / len(data)

    return -np.sum(pi * np.log2(pi))

# Entropía de las variables
def entropy_xy(X, Y, N, m):
    B = int(np.sqrt(N))
    E = np.zeros(X.shape[1])

    for j in range(B):
        for i in range(len(m)):
            if Y[j] == m[i]:
                E += (X[j, :] / N) * (X[j, :] / N) * np.log2(X[j, :] / N)

    return -E