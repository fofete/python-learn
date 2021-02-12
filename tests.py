






tipos_y_debilidades = {
  "agua": ["planta", "eléctrico"], 
  "fuego": ["agua"], 
  "planta": ["fuego", "volador", "bicho"],
  "eléctrico": ["tierra"],
  "volador": ["eléctrico"],
  "bicho": ["fuego", "volador"],
  "tierra": ["agua", "planta"]
}                                                                                       


def calcular(pokemon_tipo):                       
    return tipos_y_debilidades.get(pokemon_tipo)
 
while True:
    tipo = input("Escribe el tipo del Pokémon y recibirás sus debilidades: ")
    debilidades = calcular(tipo.strip().lower())
    if debilidades is None:
        print('El tipo', tipo, 'no se ha implementado')
    else:
        print('Las debilidades para', tipo, 'son:', debilidades)
        




# Si usas .get no puedes usar una lista, como en [pokemon_tipo] en cambio si puedes usar .get con (pokemon_tipo)
# e.j: return tipos_y_debilidades.get(pokemon_tipo) o return tipos_y_debilidades[pokemon_tipo]
# Tengo que dar un input de dos tipos y me tiene que dar un output de sus debilidades e.j: 'tierra, agua' ['planta, eléctrico']