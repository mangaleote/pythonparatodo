simbolos = ['¿','?','.','.',';',':','¡','!']
numpalabras = 0
dpalabras = dict()
with open('./citas.txt','r') as fichero:
    for linea in fichero:
        for simbolo in simbolos:
            linea = linea.replace(simbolo,' ')
        palabras = linea.split()
        for palabra in palabras:
            numpalabras += 1
            dpalabras[palabra] = dpalabras.get(palabra , 0) + 1
print('El texto contiene %s palabras' %numpalabras)
print('Las palabras se han repetido de la siguiente forma:')
for palabra in dpalabras:
    veces = 'veces'
    if dpalabras[palabra] == 1:
        veces = 'vez'
    print('La palabra "%s" se ha repetido %s %s' %(palabra, dpalabras[palabra], veces))
