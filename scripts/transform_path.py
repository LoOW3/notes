import json

def transform_path(input_file, output_file):
    # Leer el archivo de entrada JSON
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Crear la lista "path" transformada
    transformed_path = []
    for feature in data['path']:
        # Extraer el id de properties y las coordenadas
        id = str(feature['properties']['id'])
        lng = feature['geometry']['coordinates'][0]
        lat = feature['geometry']['coordinates'][1]

        # Crear un nuevo diccionario con el formato requerido
        transformed_path.append({
            "id": id,
            "lat": lat,
            "lng": lng
        })

    # Crear el objeto de salida
    output_data = {
        "path": transformed_path
    }

    # Guardar el resultado en el archivo de salida
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

if __name__ == "__main__":
    input_file = input("Ingrese el nombre del archivo de entrada: ")
    output_file = input("Ingrese el nombre del archivo JSON de salida: ")

    transform_path(input_file, output_file)
    print(f"Archivo '{output_file}' creado con éxito.")
