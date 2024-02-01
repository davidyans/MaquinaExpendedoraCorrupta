from MaquinaExpendedora import MaquinaExpendedora

def main():

    maquina_expendedora = MaquinaExpendedora()
    
    terminar = False
    while(terminar == False):
        monedas = input("Ingrese las monedas (5, 10, 25 o 50) separadas por un espacio, y un \".\" al final: ").split(" ")
        print(maquina_expendedora.procesar_monedas(monedas))
        print("######################################")
        terminar = "-" in str(input("######## Ingrese un \"-\" para finalizar el programa: "))
        print()

    print("¡Gracias por usar la máquina expendedora!")

if __name__ == "__main__":
    main()