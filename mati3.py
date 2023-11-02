import numpy as np

# new_X = topk-variables

# Paso 1: SVD
# (1) Centrar en media la data X
mean_x = np.mean(new_X, axis=0)
centered_X = new_X - mean_x

# (2) Normalizar la data X
N = new_X.shape[0]
normalized_X = centered_X / np.sqrt(N - 1)

# (3) Descomposición de la data Y
U, S, VT = np.linalg.svd(normalized_X)

# Paso 2: Seleccionar las top-k valores singulares
k = 5  # Número de valores singulares a seleccionar

# Asegurarse de que k no sea mayor que el número de características
k = min(k, new_X.shape[1])

# Reducir la dimensión de X
reduced_X = np.dot(normalized_X, VT.T[:, :k])
