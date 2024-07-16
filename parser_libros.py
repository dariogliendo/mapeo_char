from tika import parser
import sys
import regex 
import json

def separar_palabras(texto):
  pattern = r'\b[\w\p{L}]+\b'
  return regex.findall(pattern, texto)

def write_to_file(path, text):
  if not isinstance(text, str):
    text = json.dumps(text)
  print(text)
  f = open(path, "w")
  f.write(text)
  f.close()

def scrap():
  if len(sys.argv) != 2:
    print("Se debe ejecutar con sólo un argumento, indicando el path al archivo a scrapear")
    return
  archivo = sys.argv[1]
  parsed = parser.from_file(archivo)
  palabras = separar_palabras(parsed["content"])
  puntuadas = []
  for palabra in list(map(lambda x: x.lower(), palabras)):
    encontrada = next((pal for pal in puntuadas if pal["palabra"] == palabra), False)
    if not encontrada:
      puntuadas.append({
        "palabra": palabra,
        "contador": 1
      })
    else:
      encontrada["contador"] += 1
  puntuadas.sort(reverse=False, key=lambda x: x["contador"])
  write_to_file("coso.txt", puntuadas)
  
scrap()