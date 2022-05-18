import random


def play(number_system):
    number_system=number_system
    number=input("\nAdivina el numero entre el 1 y el 50.\n")
    number=number.strip()
    
    if number.isdigit():
        if int(number)<1 or int(number)>50:
            print("Escribe un numero que este dentro del rango.\n")
            play(number_system)
        else:
            if int(number)<number_system:
                print("Intenta un numero mayor.\n")
                play(number_system)
            elif int(number)>number_system:
                print("Intenta un numero menor.\n")
                play(number_system)
            else:
                print("¡¡Felicidades!! Eres un mago.\n")
                start()
    else:
        print("Escribe un numero valido, sin letras ni puntos. Vuelve a intentarlo.\n")
        play(number_system)
        


def start():
    answer=input("""¿Quieres continuar en el juego?
                 
1- Si
2- No

""")
    
    if answer != str(1) and answer != str(2):
        print("Escribe una opcion valida.\n")
        start()
    else:
        if int(answer) == 1:
            print("\n")
            number_system=random.randint(1,50)
            play(number_system)
        else:
            print("Hasta la proxima!\n")
            


def run():
    print("Bienvenido a ADIVINA EL NÚMERO!!.\n")
    start()


if __name__ == '__main__':
    run()