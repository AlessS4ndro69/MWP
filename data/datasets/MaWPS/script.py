import json

# Datos en formato JSON

def get_statements():
    with open("questions.json", "r") as archivo:
        data = json.load(archivo)
        # Extraer las preguntas
        questions = [item["sQuestion"] for item in data]

        # Escribir las preguntas en un archivo de texto
        with open("preguntas.txt", "w") as file:
            file.write("\n".join(questions))

        print("Archivo de preguntas generado: preguntas.txt")

def set_statements():
    lineas = []
    with open("preguntas_traducidas.txt","r") as file:
        lineas = file.readlines()

    with open("questions.json", "r") as archivo:
        data = json.load(archivo)
        i = 0
        for item in data:
            line = lineas[i]
            #line = line.encode('utf-8').decode('unicode-escape')
            item["sQuestion"] = line 
            print(item["sQuestion"]," >> questions.json")
            i=i+1

    with open("questions_spanish.json", "w",encoding="utf-8") as archivo_json:
        json.dump(data, archivo_json, indent=4, ensure_ascii=False)  # 'indent' para formatear con sangría
    print("JSON editado y guardado con éxito.")

if __name__ == "__main__":
    set_statements()