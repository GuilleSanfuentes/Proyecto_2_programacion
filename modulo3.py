def registro_al_tour():
    registro_tour = 0
    while int(registro_tour) <= 4:
        if registro_tour > 2:
            tercero_o_cuarto_tour = registro_tour - 2
            subtotal_tour = registro_tour - tercero_o_cuarto_tour
            costo_total_tour = (subtotal_tour * 30) + (tercero_o_cuarto_tour * (30 - (30 * 0,1)))
        else: 
            costo_total_tour = registro_tour * 30
    else: print('Se puede hasta un maximo de 4 personas')
        


def main():  
    dni = input('''Por favor, indique su DNI: ''')
    while dni.isnumeric() == True: 
        f = open('modulo3.txt', 'r')
        personas = f.read()
        f.close
        print(personas)
        for persona in personas:
            while dni == persona:
                opcion = input(''' 
                Buen dia, y bienvenid@ a la seleccion de toures que Saman Caribbean ofrece. 
                Por favor, seleccione una opcion de Tour que desee realizar:
                1. Tour en el puerto
                2. Degustación de comida local
                3. Trotar por el pueblo/ciudad
                4. Visita a lugares históricos
                5. Salir
                >''')
                if opcion == '1':
                    registro_tour = input('''Cuantas personas van a ir? ''')
                    while registro_tour.isnumeric() == True:
                        registro_tour = int(registro_tour)
                        while registro_tour <= 4:
                            while registro_tour > 2:
                                tercero_o_cuarto_tour = registro_tour - 2
                                subtotal_tour = registro_tour - tercero_o_cuarto_tour
                                costo_total_tour = (subtotal_tour * 30) + (tercero_o_cuarto_tour * (30 - (30 * 0.1)))
                                break
                            else: 
                                costo_total_tour = registro_tour * 30
                                break
                            break
                        else: print('Se puede hasta un maximo de 4 personas') 
                        break               
                    else: print('Favor, ingresar un numero de personas')
                    break
                #elif opcion == '2':
                elif opcion == '5':
                    print('Hasta Luego!')
                    break
            else: 
                f = open("modulo3.txt", "a")
                f.write(dni)
                f.close
    else: print('Favor, ingresar un DNI valido')




main()
