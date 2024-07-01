def dividir_array(array, indice):
  arr1 = []
  arr2 = []
  for i in range(0, indice):
    arr1.append(array[i])
  for i in range(indice, len(array)):
    arr2.append(array[i])
  return [arr1, arr2]

def crear_diccionario():
  archivo = open('./es.txt')
  palabras = archivo.read()
  archivo.close()
  diccionario = palabras.split("\n")
  return [palabra for palabra in diccionario if "ñ" not in palabra]