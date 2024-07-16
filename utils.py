import json

def dividir_array(array, indice):
  arr1 = []
  arr2 = []
  for i in range(0, indice):
    arr1.append(array[i])
  for i in range(indice, len(array)):
    arr2.append(array[i])
  return [arr1, arr2]

def crear_diccionario(path):
  archivo = open(path)
  palabras_json = archivo.read()
  diccionario_puntuado = json.loads(palabras_json)
  diccionario = [palabra["palabra"] for palabra in diccionario_puntuado]
  archivo.close()
  return [palabra for palabra in diccionario if "ñ" not in palabra]