import requests
if __name__ == '__main__':
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
    args = {'name', 'route', 'departure', 'cost', 'rooms', 'capacity', 'sells'}

    response = requests.get(url)

def variables():
    cruceros = response.json()
    crucero = cruceros[count]
    with open(listas_cruceros) as f:
        f.write(listas_cruceros)
            


#        nombre_1 = crucero1.get('name')
#        ruta_1 = crucero1.get('route')
#        fecha_salida_1 = crucero1.get('departure')
#        costo_1 = crucero1.get('costo')
#        rooms_1 = crucero1.get('rooms')
#        capacidad_1 = crucero1.get('capacity')
#        ventas_1 = crucero1.get('sells')
#        print(crucero1(name))