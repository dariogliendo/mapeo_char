mapa = {}

def crear_diccionario():
  archivo = open('./es.txt')
  palabras = archivo.read()
  archivo.close()
  diccionario = palabras.split("\n")
  return [palabra for palabra in diccionario if "ñ" not in palabra]

diccionario = crear_diccionario()

mapa['1a'] = {'0' : ['r'],
              '1' : ['t','d'],
              '2' : ['n'],
              '3' : ['m'],
              '4' : ['c', 'k', 'q'],
              '5' : ['l'],
              '6' : ['s','c'],
              '7' : ['f','j'],
              '8' : ['g','ch'],
              '9' : ['p','b','v']
            }

mapa['a1'] = {'b' : '9',
              'c' : '4',
              'd' : '1',
              'f' : '7',
              'g' : '8',
              'ch': '8',
              'j' : '7',
              'k' : '4',
              'l' : '5',
              'm' : '3',
              'n' : '2',
              'ñ' : '2',
              'p' : '9',
              'q' : '4',
              'r' : '0',
              's' : '6',
              't' : '1',
              'v' : '9',
              'z' : '6'
            }

def letras_a_numeros(texto):
    resultado = []
    ultimo_es_c = False;
    for letra in texto:
      if letra == 'c':
        ultimo_es_c = True;
      else:
        if ultimo_es_c and letra == 'h':
          length = len(resultado)
          resultado[length - 1] = '8'
        ultimo_es_c = False;
      if letra in mapa['a1']:
        resultado.append(mapa['a1'][letra])
    print(''.join(resultado))
    
def buscar_palabras(consonantes):
  global diccionario
  palabras = []
  for palabra in diccionario:
    valida = True
    for lista_letra in consonantes:
      for letra in lista_letra:
        if letra not in palabra:
          valida = False
    if valida is True:
      palabras.append(palabra)
  print(palabras)
    
def numeros_a_frase(numeros):
  consonantes = []
  for numero in str(numeros):
    consonantes.append(mapa['1a'][numero])
  palabras = buscar_palabras(consonantes)
  return palabras

numeros_a_frase(57)