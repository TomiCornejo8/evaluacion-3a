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
    X = np.genfromtxt('KDDTrain.txt', delimiter=',',dtype=None,encoding='utf-8')

    # Se transforma la variable 2, el protocolo a númerico
    
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
    print(param)
       
if __name__ == '__main__':   
    main()

#-------------------------------------------------------------------
