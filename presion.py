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
    
    print("\nEn las siguientes peticiones por favor llenarla con numeros enteros o decimales\n")

    profundidad = input("\n¿Cual es la profundidad en pies total del pozo?:\t")
    assert profundidad.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    profundidad = float(profundidad)

    ti_cabeza = input("\n¿Cual es la temperatura de cabeza en grados Farenheit del pozo?:\t")
    assert ti_cabeza.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    ti_cabeza = float(ti_cabeza)

    ti_fondo = input("\n¿Cual es la temperatura de fondo en grados Farenheit del pozo?:\t")
    assert ti_fondo.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    ti_fondo = float(ti_fondo)

    presion_cabeza = input("\n¿Cual es la presion en psia del pozo?:\t")
    assert presion_cabeza.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    presion_cabeza = float(presion_cabeza)

    qo = input("\n¿Cual es el gasto de aceite en barriles por dia del pozo?:\t")
    assert qo.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    qo = float(qo)

    ygt = input("\n¿Cual es la densidad relativa del gas total (los valores van entre 0 y 1)?:\t")
    assert ygt.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos o valores dentro del rango"
    ygt = float(ygt)
    assert ygt >= float(0.0) and ygt <= float(1.0), "\n\nPor favor ingresa valores dentro del rango"
    
    rugosidad = input("\n¿Cual es la rugosidad de la tuberia?:\t")
    assert rugosidad.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    rugosidad = float(rugosidad)
    assert rugosidad >= float(0.0) and rugosidad <= float(1.0), "\n\nPor favor ingresa valores dentro del rango"   

def propiedades_vazquez():
    pass


if __name__ == "__main__":
    run ()
