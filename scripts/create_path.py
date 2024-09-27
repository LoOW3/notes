import json

def create_ordered_path(index_file, points_file, output_file):
    # Leer los índices desde el archivo de texto
    with open(index_file, 'r') as f:
        indices = [line.strip() for line in f.readlines()]

    # Leer los puntos desde el archivo JSON
    with open(points_file, 'r') as f:
        points = json.load(f)

    # Crear un diccionario para acceder a los puntos por ID
    points_dict = {point['id']: point for point in points}

    # Crear la lista "path" ordenada
    ordered_path = []
    for index in indices:
        if index in points_dict:
            ordered_path.append(points_dict[index])

    # Crear el objeto de salida
    output_data = {
        "path": ordered_path
    }

    # Guardar el resultado en el archivo de salida
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

if __name__ == "__main__":
    index_file = input("Ingrese el nombre del archivo con los índices: ")
    points_file = input("Ingrese el nombre del archivo con los puntos: ")
    output_file = input("Ingrese el nombre del archivo JSON de salida: ")

    create_ordered_path(index_file, points_file, output_file)
    print(f"Archivo '{output_file}' creado con éxito.")
