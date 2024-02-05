from MaquinaExpendedora import MaquinaExpendedora

def main():

    maquina_expendedora = MaquinaExpendedora()
    #asdas
    terminar = False
    while(terminar == False):
        print("################################### Maquina expendedora corrupta ###################################")
        print("Precios: \n 1. Chicle -> 10 ctvs\n 2. Papas Rufles -> 25 ctvs\n 3. Tango -> 50 ctvs")
        monedas = input("Ingrese las monedas (5, 10, 25 o 50) y un \".\" al final, TODO separadas por un espacio: ").split(" ")
        print(maquina_expendedora.procesar_monedas(monedas))
        terminar = "-" in str(input(" ------> Ingrese un \"-\" para finalizar el programa, cualquier otra tecla para continuar comprando: "))
        print()

    print("¡Gracias por usar la máquina expendedora!")

if __name__ == "__main__":
    main()