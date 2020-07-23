import requests
if __name__ == '__main__':
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
    args = {'name', 'route', 'departure', 'cost', 'rooms', 'capacity', 'sells'}

    response = requests.get(url)

def main():
    cantidad = 1
    count = 0
    print("Por favor, indique el numero del crucero que desee averiguar: ")
    while count < cantidad:
        cruceros = response.json()
        crucero = cruceros[count]
        cantidad = len(cruceros)
        count = count + 1
        print (f"{count} {crucero.get('name')}") 
    else:
        eleccion = input()
        verificacion = eleccion.isnumeric()
        if verificacion == True:
            eleccion = int(eleccion)
            if eleccion < count:
                eleccion = eleccion - 1
                crucero = cruceros[eleccion]
                costos = crucero.get('cost')
                habitaciones = crucero.get('rooms')
                capacity = crucero.get('capacity')
                for costo in costos: 
                    num_habitaciones_basicas = habitaciones['simple']
                    total_habitaciones_basicas = num_habitaciones_basicas[0] * num_habitaciones_basicas[1]
                    num_habitaciones_premium = habitaciones['premium']
                    total_habitaciones_premium = num_habitaciones_premium[0] * num_habitaciones_premium[1]
                    num_habitaciones_vip = habitaciones['vip']
                    total_habitaciones_vip = num_habitaciones_vip[0] * num_habitaciones_vip[1]
                    for capacidad in capacity:
                        print (f"\nEl crucero ''{crucero.get('name')}'' pasa por: \n\n{crucero.get('route')} \n\nSale el {crucero.get('departure')}, y sus tikets tienen costos de habitacion de: \n\n{costos.get('simple')}$ la Básica (Hay {total_habitaciones_basicas} habitaciones, y caben {capacity.get('simple')} personas)\n\n{costos.get('premium')}$ la Premium (Hay {total_habitaciones_premium} habitaciones, y caben {capacity.get('premium')} personas)\n\n{costos.get('vip')}$ la VIP (Hay {total_habitaciones_vip} habitaciones, y caben {capacity.get('vip')} personas).")
                        if crucero.get('name') == "La Reina Isabel":
                            print('''\n!Isa! !Te quiero mucho! Aqui tienes el EasterEGG, como prometido. \nRecuerda: Aún falta hacer verdad lo prometido por sharks''')
                            break
                        else: break
                    break
            else: print(f'Por favor introduzca un numero entre el 1 y el {count}')
        else: print('Por favor, introduzca un numero') 

#   Me hubiese gustado hacerlo ara que no se parara nunca.



main()