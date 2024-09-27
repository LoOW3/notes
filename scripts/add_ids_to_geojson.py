import json

def add_ids_to_geojson(input_file, output_json_file, output_geojson_file):
    # Leer el archivo GeoJSON de entrada
    with open(input_file, 'r') as f:
        geojson_data = json.load(f)

    # Comprobar que el archivo tiene la estructura esperada
    if geojson_data['type'] != "FeatureCollection":
        raise ValueError("El archivo no es un FeatureCollection válido.")

    features = geojson_data['features']
    
    # Crear un nuevo listado con los objetos para JSON
    new_json_features = []
    # Crear un nuevo listado con las features para GeoJSON
    new_geojson_features = []

    for index, feature in enumerate(features):
        # Obtener las coordenadas
        lat = feature['geometry']['coordinates'][1]
        lng = feature['geometry']['coordinates'][0]
        
        # Crear un nuevo objeto con la estructura deseada para JSON
        new_json_feature = {
            "id": str(index + 1),  # ID como cadena, comenzando en 1
            "lat": lat,
            "lng": lng
        }
        new_json_features.append(new_json_feature)

        # Crear un nuevo objeto con la estructura original pero con ID en propiedades
        new_geojson_feature = {
            "type": "Feature",
            "id": feature['id'],
            "geometry": feature['geometry'],
            "properties": {
                "id": index + 1  # ID como entero, comenzando en 1
            }
        }
        new_geojson_features.append(new_geojson_feature)

    # Guardar el nuevo listado en el archivo de salida como JSON
    with open(output_json_file, 'w') as f:
        json.dump(new_json_features, f, indent=2)

    # Crear la estructura de FeatureCollection para el archivo GeoJSON
    new_geojson_data = {
        "type": "FeatureCollection",
        "features": new_geojson_features
    }

    # Guardar el nuevo listado en el archivo de salida como GeoJSON
    with open(output_geojson_file, 'w') as f:
        json.dump(new_geojson_data, f, indent=2)

if __name__ == "__main__":
    input_file = input("Ingrese el nombre del archivo GeoJSON de entrada: ")
    output_json_file = input("Ingrese el nombre del archivo JSON de salida: ")
    output_geojson_file = input("Ingrese el nombre del archivo GeoJSON de salida: ")
    
    add_ids_to_geojson(input_file, output_json_file, output_geojson_file)
    print(f"Archivos '{output_json_file}' y '{output_geojson_file}' creados con éxito.")
