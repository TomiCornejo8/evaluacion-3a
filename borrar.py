import numpy as np

X = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])  # Este es tu vector X de ejemplo
# X = np.array([0,1,2,3,1,1,2,3,4])
N = len(X)
B = int(np.sqrt(N))  # Calcula B como la raíz cuadrada de N

# Calcula la resolución
resolucion = (np.max(X) - np.min(X)) / (B - 1)

# Calcula los límites de los intervalos
intervalos = (np.arange(B) * resolucion) + np.min(X)

intervalos[B-1] = intervalos[B-1] + 1 

print(f"B = {B}")
print(f"N° Intervalos = {len(intervalos)}")
print(f"Intervalos = {intervalos}")

particiones = np.digitize(X, intervalos) - 1

# Obtenemos los valores unicos del atributo
unique_values = np.unique(particiones)

# Calculamos la "entropia"
for value in unique_values:
    subset_indices = np.where(particiones == value)
    subset_data = X[subset_indices]
    print(f"({value+1}) {subset_data}")