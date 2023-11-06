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
    data = np.genfromtxt('KDDTrain.txt', delimiter=',',dtype=str,encoding='utf-8')

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
    var_42 = data[:, 41]

    # Se crea una nueva matriz para almacenar los valores numéricos de la clase (1, 2 ó 3)
    new_var_42 = np.zeros_like(var_42)

    # Mapear las categorías a los valores numéricos
    for valor, clase_lista in clase.items():
        new_var_42[np.isin(var_42, clase_lista)] = valor

    # Reemplazar la columna original con los valores numéricos
    Y = new_var_42

    # Transformar variables categoricas a numeros enteros
    # Se saca la matriz de caracteristicas
    X = data[:,:41]
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
    
    return rsvd.norm_data(X.astype(float)),Y

# selecting variables
def select_vars(X,Y,param):
    # Se randomiza las muestras de la BD
    random_index = np.genfromtxt('idx_samples.csv', delimiter=',',dtype=int,encoding='utf-8')
    # Se pasan posciones de 0 a n-1
    random_index -= 1
    # Se aplica el random a las muestras 
    X = X[random_index, :]
    Y = Y[random_index]

    # Se toman solo las clases indicadas en el archivo de configuración
    m = np.where(np.array([param[3],param[4],param[5]]) == 1)[0] + 1
    selected_index = np.where(np.isin(Y,m.astype(str)))[0]
    X = X[selected_index,:]
    Y = (Y[selected_index]).astype(int)
    
    # Se corta al N° de muestras pedido en los parametros
    N = param[0]
    if(N <= X.shape[0]):
        X = X[:N]
        Y = Y[:N]
    else:
        N = X.shape[0]

    # Se calcula la información estimada
    I = ig.inform_estimate(Y)
    
    # Se calcula la entropia, y ganacia de la información
    IG = np.zeros(X.shape[1])
    for j in range(X.shape[1]):
        E = ig.entropy_xy(X[:,j],Y)
        IG[j] = I - E

    # Ordenamos por los top-k relevantes, y asignamos el nuevo X
    K = param[1]
    # Se ordenan los IG decrecientemente
    idx = np.argsort(IG)[::-1]
    IG = IG[idx]
    # Se ordenan y se cortan los K valores relevancia
    X = (X[:,idx])[:,:K]

    # SVD

    # Centrar en media la data X.
    for j in range(X.shape[1]):
        x_mean = np.mean(X[:,j])
        X[:,j] = X[:,j] - x_mean
    
    # Se normaliza X
    X_norm = X / np.sqrt(N - 1)

    V = rsvd.svd_data(X_norm) 

    k = param[2]
    X = np.dot(X,V[:, :k])

    return IG,idx,V[:, :k]

#save results
def save_results(gain,idx,V):
    np.savetxt("gain_values.csv", gain, delimiter=',', fmt='%f')
    np.savetxt("gain_idx.csv", idx, delimiter=',', fmt='%d')
    np.savetxt("filter_v.csv", V, delimiter=',', fmt='%f')
    return

#-------------------------------------------------------------------
# Beginning ...
def main():
    param = load_config()            
    X,Y = load_data()
    [gain, idx, V]= select_vars(X,Y,param)                 
    save_results(gain,idx,V)
       
if __name__ == '__main__':   
    main()

#-------------------------------------------------------------------