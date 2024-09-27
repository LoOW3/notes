import json
import math

def calculate_distance(lat1, lng1, lat2, lng2):
    # Calcular la distancia entre dos puntos (en metros)
    R = 6371000  # Radio de la Tierra en metros
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lng = math.radians(lng2 - lng1)

    a = (math.sin(delta_lat / 2) ** 2 +
         math.cos(lat1_rad) * math.cos(lat2_rad) *
         math.sin(delta_lng / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def create_nodes_and_links(points, connections):
    nodes = points
    links = {}
    
    points_dict = {point['id']: point for point in points}

    for line in connections.splitlines():
        line = line.strip()
        if not line or '=' not in line:
            continue  # Ignorar líneas en blanco o mal formateadas

        node, connections_str = line.split('=')
        node = node.strip()
        connected_nodes = connections_str.strip().replace('|', '').split('-')

        links[node] = []
        for connected_node in connected_nodes:
            connected_node = connected_node.strip()
            if connected_node in points_dict:
                lat1, lng1 = points_dict[node]['lat'], points_dict[node]['lng']
                lat2, lng2 = points_dict[connected_node]['lat'], points_dict[connected_node]['lng']
                distance = calculate_distance(lat1, lng1, lat2, lng2)

                links[node].append({
                    "point": connected_node,
                    "distance": distance
                })

    return {"nodes": nodes, "links": links}

if __name__ == "__main__":
    points_file = input("Ingrese el nombre del archivo con los puntos: ")
    connections_file = input("Ingrese el nombre del archivo con las conexiones: ")
    output_file = input("Ingrese el nombre del archivo JSON de salida: ")

    with open(points_file, 'r') as f:
        points = json.load(f)

    with open(connections_file, 'r') as f:
        connections = f.read()

    result = create_nodes_and_links(points, connections)

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Archivo '{output_file}' creado con éxito.")
