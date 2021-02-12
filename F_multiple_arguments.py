#1 Las funciones pueden tener más de un parámetro:

def area(a, b):
    return a * b

print(area(5, 5))





#2 Las funciones pueden tener parámetros predeterminados (por ejemplo, coefficient):

def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))





#3 Los argumentos se pueden pasar como argumentos non-keyword (posicionales) (por ejemplo, a)
# o argumentos keyword (por ejemplo, b = 2 y c = 10):

def volume(a, b, c):         
    return a * b * c

print(volume(1, b=2, c=10))






#4 El parámetro *args permite llamar a la función con un número arbitrario de argumentos que no son palabras clave:

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 2, 3, 4, 5, 6))


# también:


def find_max(*args):
    return max(args) # La función max() devuelve el elemento con el valor más alto o el elemento con el valor más alto en un iterable.

print(find_max(3, 99, 1001, 2, 8))


# también x2:


def function(*args):
    args = [s.upper() for s in args]
    return sorted(args) # sorted devuelve una nueva lista que contiene todos los elementos del iterable en orden ascendente. En este caso, alfabeticalmente

print(function('nieve', 'iceberg', 'ventisca'))





#5 El parámetro **kwargs permite llamar a la función con un número arbitrario de argumentos de keywords:

def function(**kwargs):
    return kwargs

print(function(a = 1, b = 2, c = 3))

# también:

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get) # La función max() otra vez
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))