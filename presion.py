def run():
    print("Este codigo realizara los calculos necesarios para determinar la presion en cabeza o en fondo dependiendo lo que usted requiera")
    print("\nSi usted quiere la presion a la cabeza coloque 1, pero si quiere la presion en fondo coloque 2")
    
    cabezaofondo = input("\nDeme su eleccion [1] o [2]:\t")
    assert cabezaofondo.isnumeric() and int(cabezaofondo) >= 1 and int(cabezaofondo) <= 2, "\nFavor de Ingresar un numero que sea 0 o 1"
    
    cabezaofondo = int(cabezaofondo)
    
    if cabezaofondo == 1:
        print("\nUsted eligio calcular el valor de la presion en cabeza de pozo")
    else:
        print("\nUsted eligio calcular el valor de la presion en fondo de pozo")
    
    Profundidad = float(input("\n¿Cual es la profundidad en pies total del pozo?:\t"))
    Ti = float(input("\n¿Cual es la temperatura inical en Farenheit del pozo?:\t"))
    PresionInicial = float(input("\n¿Cual es la presion en psia del pozo?:\t"))

def propiedades_vazquez():
    pass


if __name__ == "__main__":
    run ()
