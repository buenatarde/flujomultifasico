def run():
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    print("Este codigo realizara los calculos necesarios para determinar la presion en cabeza o en fondo dependiendo lo que usted requiera")
    print("\nSi usted quiere la presion a la cabeza coloque 1, pero si quiere la presion en fondo coloque 2")
    
    cabezaofondo = input("\nDeme su eleccion [1] o [2]:\t")
    assert cabezaofondo.isnumeric() and int(cabezaofondo) >= 1 and int(cabezaofondo) <= 2, "\nFavor de Ingresar un numero que sea 0 o 1"
    
    cabezaofondo = int(cabezaofondo)
    
    if cabezaofondo == 1:
        print("\nUsted eligio calcular el valor de la presion en cabeza de pozo")
    else:
        print("\nUsted eligio calcular el valor de la presion en fondo de pozo")
    
    Profundidad = input("\n¿Cual es la profundidad en pies total del pozo?:\t")
    assert Profundidad.isnumeric(), "\n\nPor favor ingresa valores numericos"
    Profundidad = float(Profundidad)

    Ti = input("\n¿Cual es la temperatura inical en Farenheit del pozo?:\t")
    assert Ti.isdecimal(), "\n\nPor favor ingresa valores numericos"
    Ti = float(Ti)

    PresionInicial = input("\n¿Cual es la presion en psia del pozo?:\t")
    assert PresionInicial.isnumeric(), "\n\nPor favor ingresa valores numericos"
    PresionInicial = float(PresionInicial)

    Qo = input("\n¿Cual es el gasto de aceite en barriles por dia del pozo?:\t")
    assert Qo.isnumeric(), "\n\nPor favor ingresa valores numericos"
    Qo = float(Qo)

    ygt = input("\n¿Cual es la densidad relativa del gas total (los valores van entre 0 y 1)?:\t")
    assert ygt.isnumeric() and ygt >= float(0.0) and ygt <= float(1.0), "\n\nPor favor ingresa valores numericos o valores dentro del rango"
    ygt = float(ygt)
    
    

def propiedades_vazquez():
    pass


if __name__ == "__main__":
    run ()
