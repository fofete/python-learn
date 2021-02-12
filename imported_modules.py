                                                              ######################
                                                             ##//IMPORTED MODULES\\##
                                                              ###################### 
# Los Builtin modules son todos los objetos que están escritos dentro del intérprete de Python en lenguaje C.

# Los Builtin modules contienen builtins objects.

# Algunos Builtin modules no están disponibles de inmediato en el global namespace.
  # Son partes de un builtin module. 
   # Para usar esos objetos, el módulo debe importarse primero. P.ej.:
                                                            ####################
                                                            # --> import time  #
                                                            # --> time.sleep(5)#
                                                            ####################
# Se puede imprimir una lista de todos los builtin modules con:
                                                            ###############################
                                                            # --> import sys              #
                                                            # --> sys.builtin_module_names#
                                                            ###############################
# Las Standard libraries son una jerga que incluye tanto builtin modules escritos en C como módulos escritos en Python.

# Las Standard libraries escritas en Python residen en el directorio de instalación de Python como archivos.py
  # Puede encontrar la ruta de directorio con sys.prefix <--- "En mi caso no funciona 🤷‍♂️"

# Los Packages son una colección de modules.py

# Las libraries de terceros son Packages o módulos escritos por terceros.

# Las libraries de terceros se pueden instalar desde la terminal:
  # Windows:
            ## pip install pandas Ó python -m pip install pandas ##



# some ej.:

import time
import os
import pandas

horas_24 = 86400

while True:
    if os.path.exists("Textos/vegtables.txt"):
        with open("Textos/vegetables.txt") as file:
            print(file.read())
            time.sleep(horas_24)
    else:
        print("El archivo no existe.")
        break
         
            
# Pandas:
if True:
    if os.path.exists("Textos/temps_today.csv"):
        data = pandas.read_csv("Textos/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("El archivo no existe.")
        