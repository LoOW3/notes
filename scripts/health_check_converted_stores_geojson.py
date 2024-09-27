import json

def health_check(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    ids = set()
    missing_ids = []
    duplicate_ids = set()
    
    for index, obj in enumerate(data):
        if 'id' not in obj or not obj['id']:
            missing_ids.append(index)
        else:
            if obj['id'] in ids:
                duplicate_ids.add(obj['id'])
            else:
                ids.add(obj['id'])
    
    if missing_ids:
        print(f"Los siguientes objetos no tienen 'id': {missing_ids}")
    if duplicate_ids:
        print(f"Los siguientes 'id's están repetidos: {duplicate_ids}")
    
    if not missing_ids and not duplicate_ids:
        print("Todos los objetos tienen un 'id' único y válido.")

if __name__ == "__main__":
    file_path = input("Por favor, introduce la ruta del archivo JSON: ")
    health_check(file_path)
