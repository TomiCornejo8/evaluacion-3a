import numpy as np

# Paso 1: Calcular la Ganancia de Información IG(Y, x)
def calculate_ig(Y, X):
    # Calcular I(Y) - E(X)
    ig = calculate_information(Y) - calculate_entropy(X)
    return ig

# Paso 2: Calcular la Información Estimada de la Clase I(Y)
def calculate_information(Y):
    m = len(Y)
    unique_classes, class_counts = np.unique(Y, return_counts=True)
    probabilities = class_counts / m
    information = -np.sum(probabilities * np.log2(probabilities))
    return information

# Paso 3: Calcular la Entropía Estimada de la Variable E(X)
def calculate_entropy(X, B):
    N, D = X.shape
    entropy = 0
    for j in range(B):
        d_j = np.sum(X[:, j])
        for i in range(len(unique_classes)):
            d_ij = np.sum(X[Y == unique_classes[i], j])
            if d_ij > 0:
                entropy += (d_ij / N) * np.log2(d_ij / N)
    entropy = -entropy
    return entropy

# Paso 4: Ordenar IG y seleccionar las top-K variables relevantes
def select_top_k_features(X, Y, K, B):
    ig_values = []
    for x in range(X.shape[1]):
        ig = calculate_ig(Y, X[:, x])
        ig_values.append(ig)
    ig_values = np.array(ig_values)
    top_k_indices = np.argsort(ig_values)[::-1][:K]
    new_X = X[:, top_k_indices]
    return new_X

# Parámetros de ejemplo
N = 1000  # Número de muestras
D = 20   # Número de variables (características, atributos)
K = 10   # Número de variables relevantes a seleccionar
B = int(np.sqrt(N))  # Número de bins (intervalos)

# Generar datos de ejemplo
X = np.random.rand(N, D)
Y = np.random.randint(0, 2, N)  # Clases binarias

# Calcular las variables más relevantes
new_X = select_top_k_features(X, Y, K, B)
