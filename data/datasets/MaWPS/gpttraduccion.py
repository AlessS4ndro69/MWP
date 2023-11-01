import array
import requests
import json

# Definir la clave de la API de Google Translate (reemplaza 'TU_CLAVE_DE_API' con tu clave real)
API_KEY = "AIzaSyBtjGE3TuoWddqwVUq5LwADqk2QaxWouxI"

def goTranslate(requestText):

    # Idioma de origen y destino (en este ejemplo, de inglés a español)
    SOURCE_LANG = "en"
    TARGET_LANG = "es"

    # URL del servicio de traducción de Google
    URL = "https://translation.googleapis.com/language/translate/v2"

    # Parámetros de la solicitud
    params = {
        "key": API_KEY,
    }

    # Datos JSON para la solicitud de traducción
    data = {
        "q": requestText,
        "source": SOURCE_LANG,
        "target": TARGET_LANG,
    }

    # Realizar la solicitud de traducción usando la biblioteca requests
    response = requests.post(URL, params=params, json=data)

    # Verificar si la solicitud se realizó con éxito
    
    try:
        if response.status_code == 200:
            translation = response.json()
            translated_text = translation['data']['translations'][0]['translatedText']
            print("Texto traducido:", translated_text)
            return translated_text
    except Exception as e:
        print("Ocurrió una excepción no manejada:", str(e))



traducted_lines = []
array_lines = []
with open("preguntas.txt", "r") as reader:    
    array_lines = reader.readlines()

with open("preguntas_traducidas.txt","w") as writer:
    #writer.write("\n".join(traducted_lines))
    print("iniciando traducción")
    for line in array_lines:
        translate = goTranslate(line)
        traducted_lines.append(translate)
        writer.write(translate + "\n")
        #print(translate,">>archivo")
    print("se generado preguntas_traducidas.txt")

    



