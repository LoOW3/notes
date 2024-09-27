import json

# input usuario
input_filename = input("Ingrese el nombre del archivo GeoJSON original (con .geojson): ")
output_filename = input("Ingrese el nombre del archivo de salida (con .json): ")

# cargue de geojson
try:
    with open(input_filename, 'r') as f:
        geojson_data = json.load(f)

    output_data = []

    for feature in geojson_data['features']:
        # extraer coords de la feature
        coordinates = feature['geometry']['coordinates'][0]
        
        transformed_coordinates = [
            {
                "lng": coord[0],
                "lat": coord[1]
            } for coord in coordinates
        ]
        
        new_feature = {
            "coordinates": transformed_coordinates,
            "id": feature['properties']['name'] 
        }
        
        # llenar archive de salida
        output_data.append(new_feature)


    with open(output_filename, 'w') as f:
        json.dump(output_data, f, indent=4)

    print(f"Exitoso. Archivo {output_filename} creado.")

except FileNotFoundError:
    print(f"Error: Archivo {input_filename} no se encontró.")
except json.JSONDecodeError:
    print("Error: El archivo no es un archivo JSON válido.")

