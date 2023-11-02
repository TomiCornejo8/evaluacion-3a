import numpy as np

# Datos de ejemplo
X = np.array([['A', 'X', 'Z', 'P'],
              ['B', 'Y', 'Z', 'Q'],
              ['A', 'X', 'W', 'P'],
              ['C', 'Y', 'W', 'Q'],
              ['B', 'X', 'W', 'P'],
              ['A', 'Y', 'Z', 'Q'],
              ['C', 'X', 'Z', 'P'],
              ['A', 'X', 'W', 'P'],
              ['B', 'Y', 'W', 'Q'],
              ['C', 'Y', 'W', 'P']])

y = np.array([1, 0, 1, 0, 1, 0, 1, 1, 0, 0])

# Función para calcular la entropía de un conjunto de datos
def entropy(data):
    # Calcula la probabilidad de cada clase
    unique_classes, class_counts = np.unique(data, return_counts=True)
    class_probabilities = class_counts / len(data)
    
    # Calcula la entropía
    entropy = -np.sum(class_probabilities * np.log2(class_probabilities))
    
    return entropy

# Función para calcular la ganancia de información de un atributo
def information_gain(data, attribute_column):
    # Calcula la entropía del conjunto de datos original
    original_entropy = entropy(data)
    
    # Divide el conjunto de datos en subconjuntos según el valor del atributo
    unique_values, value_counts = np.unique(attribute_column, return_counts=True)
    weighted_entropy = 0
    
    for value in unique_values:
        subset_indices = np.where(attribute_column == value)
        subset_data = data[subset_indices]
        weighted_entropy += (len(subset_data) / len(data)) * entropy(subset_data)
    
    # Calcula la ganancia de información
    information_gain = original_entropy - weighted_entropy
    
    return information_gain

# Calcular la ganancia de información para cada columna de atributos
num_columns = X.shape[1]
information_gains = []

for i in range(num_columns):
    attribute_column = X[:, i]
    ig = information_gain(y, attribute_column)
    information_gains.append(ig)
    print(f'Ganancia de Información para atributo {i}: {ig}')

# Encuentra el índice del atributo con la mayor ganancia de información
best_attribute_index = np.argmax(information_gains)
best_attribute_name = f'Atributo {best_attribute_index}'
print(f'\nEl mejor atributo es {best_attribute_name} con una ganancia de información de {information_gains[best_attribute_index]}')
