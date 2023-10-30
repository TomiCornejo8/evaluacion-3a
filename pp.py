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
        1: ["normal"],
        # Clase 2: DOS (Denegación de Servicio) (Ataques de Denegación de Servicio):
        2: ["back","land","neptune","pod","smurf","teardrop","apache2","processtable","mailbomb","udpstorm"],
        # Clase 3: Probe (Sondeo) (Intentos de sondeo o exploración de la red):
        3: ["ipsweep","nmap","portsweep","satan","rootkit","saint","mscan"]
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

    # Se filtran las var 42 que no cumplen con ninguna clase del ppt
    condicion = (new_var_42 == "1") | (new_var_42 == "2") | (new_var_42 == "3")
    X = X[condicion]

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
    
    return rsvd.norm_data(X.astype(float))

# selecting variables
def select_vars(X,param):
    # Se randomiza las muestras de la BD
    random_index = np.random.permutation(X.shape[0])
    X = X[random_index, :]
    # Se corta al N° de muestras pedido en los parametros
    N = param[0]
    X = X[:N]

    # Array de configuración de clases
    m = np.array([1*param[3],2*param[4],3*param[5]])
    m = m[m != 0]

    # Se calcula la ganacia de información
    I = ig.inform_estimate(X,N,m)
    E = ig.entropy_xy(X,N,m,I)

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
    select_vars(X,param)    
    # [gain, idx, V]= select_vars(X,param)                 
    # save_results(gain,idx,V)
       
if __name__ == '__main__':   
    main()

#-------------------------------------------------------------------
