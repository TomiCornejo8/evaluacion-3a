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
    # var2_unicas = np.unique(X[:,1])
    # var3_unicas = np.unique(X[:,2])
    # var4_unicas = np.unique(X[:,3])
    
    return X

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
    print(X[0,41])
       
if __name__ == '__main__':   
    main()

#-------------------------------------------------------------------
