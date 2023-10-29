# Pre-proceso: Selecting variables for IDS


import numpy          as np
import inform_gain    as ig
import redundancy_svd as rsvd

# Load Parameters
def load_config():
    # Se lee el archivo CSV de configuración
    param = np.genfromtxt('cnf_sv.csv', delimiter=',', dtype=None,encoding='utf-8')
    return param

# Load data 
def load_data():
    # Se lee el data set KDDTrain
    X = np.genfromtxt('KDDTrain.txt', delimiter=',',dtype=str,encoding='utf-8')

    # Ponermos en la variable 42 su clase correspondiente
    clase = {
        # Clase 1: Normal (Tráfico legítimo):
        1: ["normal","ftp_write","imap"],
        # Clase 2: DOS (Denegación de Servicio) (Ataques de Denegación de Servicio):
        2: ["back","land","neptune","pod","smurf","teardrop","buffer_overflow","guess_passwd","phf","spy","warezclient","warezmaster"],
        # Clase 3: Probe (Sondeo) (Intentos de sondeo o exploración de la red):
        3: ["ipsweep","loadmodule","multihop","nmap","portsweep","satan","rootkit"]
    }
    # Tomamos la variable 42 tipo de tráfico.
    var_42 = X[:, 41]

    # Se crea una nueva matriz para almacenar los valores numéricos de la clase (1, 2 ó 3)
    new_var_42 = np.zeros_like(var_42)

    # Mapear las categorías a los valores numéricos
    for valor, clase_lista in clase.items():
        new_var_42[np.isin(var_42, clase_lista)] = valor

    # Reemplazar la columna original con los valores numéricos
    X[:, 41] = new_var_42

    # Transformar variables categoricas a numeros enteros
    # Encontramos los valores únicos de cada variable
    var2_unicas = np.unique(X[:,1])
    var3_unicas = np.unique(X[:,2])
    var4_unicas = np.unique(X[:,3])

    # Mapeamos cada valor único con un número dentro de un diccionario de python
    mapeo2 = {valor: indice for indice, valor in enumerate(var2_unicas,start=1)}
    mapeo3 = {valor: indice for indice, valor in enumerate(var3_unicas,start=1)}
    mapeo4 = {valor: indice for indice, valor in enumerate(var4_unicas,start=1)}
    
    for fila in X:
        fila[1] = mapeo2[fila[1]]
        fila[2] = mapeo3[fila[2]]
        fila[3] = mapeo4[fila[3]]
    
    X_float = X.astype(float)
    
    # Definimos los valores de a y b
    a = 0.01
    b = 0.99

    # Calcula los valores mínimos y máximos de las columnas 1 a 41
    x_min = X_float[:, 0:41].min(axis=0)
    x_max = X_float[:, 0:41].max(axis=0)

    x_max[x_max == x_min] += 1e-20 # Para evitar divisiones con 0

    # Realiza la normalización para las columnas 1 a 41
    X_float[:, 0:41] = ((X_float[:, 0:41] - x_min) / (x_max - x_min)) * (b - a) + a

    return X_float

# selecting variables
def select_vars():
    ...
    return()

#save results
def save_results():
    ...
    return

#-------------------------------------------------------------------
# Beginning ...
def main():
    param = load_config()            
    X = load_data()   
    # [gain, idx, V]= select_vars(X,param)                 
    # save_results(gain,idx,V)
    print(X[0])
       
if __name__ == '__main__':   
    main()

#-------------------------------------------------------------------
