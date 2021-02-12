#1 Puedes leer un archivo existente con Python:

with open("file.txt") as file:
    content = file.read()




#2 Puedes crear un nuevo archivo con Python y escribir algo de texto en él:

with open("file.txt", "w") as file:
    content = file.write("Sample text")




#3 Puedes agregar texto a un archivo existente sin sobrescribirlo:

with open("file.txt", "a") as file:
    content = file.write("More sample text")




#4 Puedes agregar y leer un archivo con:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()