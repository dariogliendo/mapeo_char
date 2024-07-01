from utils import dividir_array, crear_diccionario
from mapas import num_a_letra, letra_a_num

diccionario = crear_diccionario()

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
      if letra in letra_a_num:
        resultado.append(letra_a_num[letra])
    print(''.join(resultado))

def buscar_parcial(consonantes, diccionario):
  palabras_aptas = []
  for palabra in diccionario:
    consonantes_palabra = [letra for letra in palabra if letra not in ['a', 'e', 'i', 'o', 'u']]
    valida = True;
    if len(consonantes_palabra) != len(consonantes):
      valida = False
      continue
    for idx, cons_palabra in enumerate(consonantes_palabra):
      if cons_palabra not in consonantes[idx]:
        valida = False
    if valida:
      palabras_aptas.append(palabra)
  return palabras_aptas
    
def buscar_palabras(consonantes, lista_palabras = []):
  global diccionario
  palabras = buscar_parcial(consonantes, diccionario)
  if len(palabras):
    lista_palabras.append(palabras[0])
    
def numeros_a_frase(numeros):
  consonantes = []
  for numero in str(numeros):
    consonantes.append(num_a_letra[numero])
  palabras = buscar_palabras(consonantes)
  print(palabras)
  return palabras

numeros_a_frase(37999385)