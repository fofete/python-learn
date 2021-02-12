#Dividir de forma rápida los números de una lista

temps = [231, 223, 340, 230]

new_temps = [temp / 10 for temp in temps] #Dividimos los números de una lista, en este caso temps / 10

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
print(new_temps)



#Eliminar el número deseado de una lista 

temps = [231, 223, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999] #Eliminamos el -9999

print(new_temps)



#Intercambiar un número por otro en una lista

temps = [231, 223, 340, -9999, 230]

new_temps = [temp / 10 if temp != -9999 else 1 for temp in temps] #Cambiamos el -9999 por un 1

print(new_temps)