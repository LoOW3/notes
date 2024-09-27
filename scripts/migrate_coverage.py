import json

def move_polygon(geojson, move_amount):
    """
    Mueve las coordenadas de un polígono en un GeoJSON y devuelve un nuevo GeoJSON.

    :param geojson: GeoJSON como un diccionario.
    :param move_amount: Tupla (longitud, latitud) para mover el polígono.
    :return: Nuevo GeoJSON con las coordenadas movidas.
    """
    longitude_move, latitude_move = move_amount

    # Crear una nueva estructura de GeoJSON
    new_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    # Iterar sobre las características del GeoJSON original
    for feature in geojson['features']:
        new_feature = {
            "type": "Feature",
            "id": feature['id'],
            "geometry": {
                "type": feature['geometry']['type'],
                "coordinates": []
            },
            "properties": feature['properties']
        }

        if feature['geometry']['type'] == 'Polygon':
            # Mover cada coordenada y agregarla al nuevo GeoJSON
            new_coordinates = []
            for coord in feature['geometry']['coordinates'][0]:
                lon, lat = coord
                new_coordinates.append([lon + longitude_move, lat + latitude_move])
            new_feature['geometry']['coordinates'].append(new_coordinates)

        new_geojson['features'].append(new_feature)

    return new_geojson

# Ejemplo de uso
geojson_data = {
  "type": "FeatureCollection",
  "id": "sm1dc7c1e7",
  "features": [
    {
      "type": "Feature",
      "id": "sm76085d9c",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -74.102115176,
              4.631713397
            ],
            [
              -74.102221661,
              4.633400406
            ],
            [
              -74.102539438,
              4.635060806
            ],
            [
              -74.103063496,
              4.636668411
            ],
            [
              -74.103785568,
              4.63819787
            ],
            [
              -74.104694269,
              4.639625063
            ],
            [
              -74.105775266,
              4.640927481
            ],
            [
              -74.107011513,
              4.642084587
            ],
            [
              -74.108383512,
              4.643078132
            ],
            [
              -74.109869627,
              4.643892449
            ],
            [
              -74.111446421,
              4.644514696
            ],
            [
              -74.113089027,
              4.644935061
            ],
            [
              -74.114771539,
              4.645146913
            ],
            [
              -74.116467423,
              4.645146913
            ],
            [
              -74.118149935,
              4.644935061
            ],
            [
              -74.119792541,
              4.644514696
            ],
            [
              -74.121369335,
              4.643892449
            ],
            [
              -74.12285545,
              4.643078132
            ],
            [
              -74.124227449,
              4.642084587
            ],
            [
              -74.125463696,
              4.640927481
            ],
            [
              -74.126544693,
              4.639625063
            ],
            [
              -74.127453394,
              4.63819787
            ],
            [
              -74.128175466,
              4.636668411
            ],
            [
              -74.128699524,
              4.635060806
            ],
            [
              -74.129017301,
              4.633400406
            ],
            [
              -74.129123786,
              4.631713397
            ],
            [
              -74.129017301,
              4.630026384
            ],
            [
              -74.128699524,
              4.628365972
            ],
            [
              -74.128175466,
              4.626758348
            ],
            [
              -74.127453394,
              4.625228864
            ],
            [
              -74.126544693,
              4.623801643
            ],
            [
              -74.125463696,
              4.622499193
            ],
            [
              -74.124227449,
              4.621342055
            ],
            [
              -74.12285545,
              4.620348479
            ],
            [
              -74.121369335,
              4.619534135
            ],
            [
              -74.119792541,
              4.618911866
            ],
            [
              -74.118149935,
              4.618491486
            ],
            [
              -74.116467423,
              4.618279625
            ],
            [
              -74.114771539,
              4.618279625
            ],
            [
              -74.113089027,
              4.618491486
            ],
            [
              -74.111446421,
              4.618911866
            ],
            [
              -74.109869627,
              4.619534135
            ],
            [
              -74.108383512,
              4.620348479
            ],
            [
              -74.107011513,
              4.621342055
            ],
            [
              -74.105775266,
              4.622499193
            ],
            [
              -74.104694269,
              4.623801643
            ],
            [
              -74.103785568,
              4.625228864
            ],
            [
              -74.103063496,
              4.626758348
            ],
            [
              -74.102539438,
              4.628365972
            ],
            [
              -74.102221661,
              4.630026384
            ],
            [
              -74.102115176,
              4.631713397
            ]
          ]
        ]
      },
      "properties": {
        "name": "COBERTURA"
      }
    }
  ]
}
move_amount = (0.03701133046458, 0.034151694124067)
moved_geojson = move_polygon(geojson_data, move_amount)

# Imprimir el nuevo GeoJSON
print(json.dumps(moved_geojson, indent=2))
