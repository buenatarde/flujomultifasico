import numpy as np  
import matplotlib as plt
import pandas as pd


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
    
    error =  input("\n¿Que error es el aceptable para usted en porcentaje?:\t")
    assert error.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    error = float(error)
    error = error/100


    print("\nEn las siguientes peticiones por favor llenarla con numeros enteros o decimales\n")

#Se empiezan a pedir los inputs del usuario los cuales se usaran para tener datos con que trabajar el modelo de presion en un pozo

    #Primero se pedira las caracterisitcas del pozo 
    profundidad = input("\n¿Cual es la profundidad en pies total del pozo?:\t")
    assert profundidad.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    profundidad = float(profundidad)

    celda = input("\n¿En cuantas celdas quieres que se divida el pozo para su analisis? (numeros enteros):\t")
    assert celda.isnumeric(), "\n\nPor favor ingresa valores numericos que sean enteros"
    celda = int(celda)

#Se pediran las propiedades inicales como presion o temperatura
    ti_cabeza = input("\n¿Cual es la temperatura de cabeza en grados Farenheit del pozo?:\t")
    assert ti_cabeza.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    ti_cabeza = float(ti_cabeza)

    ti_fondo = input("\n¿Cual es la temperatura de fondo en grados Farenheit del pozo?:\t")
    assert ti_fondo.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    ti_fondo = float(ti_fondo)

    presion_cabeza = input("\n¿Cual es la presion en psia del pozo?:\t")
    assert presion_cabeza.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    presion_cabeza = float(presion_cabeza)

#Se pedira los datos referentes al aceite o al gas
    qo = input("\n¿Cual es el gasto de aceite en barriles por dia del pozo?:\t")
    assert qo.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    qo = float(qo)

    api = input("\n¿Cuales son los grados API del aceite?:\t")
    assert api.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    api = float(api)
    assert api >= float(10.0) and api <= float(100.0), "\n\nPor favor ingresa valores dentro del rango" 

    ygt = input("\n¿Cual es la densidad relativa del gas total (los valores van entre 0 y 1)?:\t")
    assert ygt.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos o valores dentro del rango"
    ygt = float(ygt)
    assert ygt >= float(0.0) and ygt <= float(1.0), "\n\nPor favor ingresa valores dentro del rango"

    rga = input("\n¿Cual es la relacion gas aceite de tu muestra?:\t")
    assert rga.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos o valores dentro del rango"
    rga = float(rga)
    assert rga >= float(0.0), "\n\nPor favor ingresa valores positivos"
    
    rugosidad = input("\n¿Cual es la rugosidad de la tuberia?:\t")
    assert rugosidad.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    rugosidad = float(rugosidad)
    assert rugosidad >= float(0.0), "\n\nPor favor ingresa valores dentro del rango"   

 
#Se empiezan a hacer calculos que comparte los dos metodos para evitar un mayor uso de poder de calculo desperdiciado
    pendiente = profundidad/(ti_fondo-ti_cabeza)

    constanteT = -pendiente*ti_cabeza
    #SACAR EL ARREGLO DE CELDAS AL IGUAL QUE LA DETERMINACION DE LA TEMPERATURA DE LOS METODOS YA QUE INDEPENDIENTEMENETE DE CUAL ELIJAN NO CAMBAI
    celdas = np.linspace(0,profundidad,celda)
        
    print("A continuacion favor de elegir el metodo por el cual se calculara las propiedades de los fluidos")
    print("\nSi usted quiere usar el metodo de vazquez elija 1 si quiere usar el de Stnading elija 2")
    
    metodo = input("\nDeme su eleccion [1] o [2]:\t")
    assert metodo.isnumeric() and int(metodo) >= 1 and int(metodo) <= 2, "\nFavor de Ingresar un numero que sea 0 o 1"
    metodo = int(metodo)

    if metodo == 1:
        print("\nUsted eligio calcular las propiedades de los fluidos por el metodo de Vazquez")
        propiedades_vazquez #Quitar las propiedades aqui afuera y solo decirle una vez al usuario que metodo eligio 

    else:
        print("\nUsted eligio calcular las propiedades por el metodo de Standing")
        propiedades_standing
    
    T = []
    P = []
#Comienza el programa MAIN
    errorexp=1
    while errorexp < error:
        for i in celdas:
            T[0]=ti_cabeza
            pass



def propiedades_vazquez (profundidad, celda, ti_cabeza, t,p,qo,api,ygt,rga,rugosidad,pendiente,constanteT):
    if api>30:
        C1 = 0.0178; C2 = 1.187; C3 = 23.931;
        Pb = (((rga*np.exp(-C3*(api/t+460)))/(C1*ygt)))*(1/C2)
        ygd = []
        rs = []
        for i in range (0,6):
            ygd [0]=ygt
            rs[i+1] =ygd[i]*C1*(p**C2)*np.exp(C3*(api/t+460))
            ygd[i+1] = .25+.02*api+((rs[i+1]*.000001)*(0.6874-(3.5864*api)))
        ygl = ((rga*ygt)-(rs[6]*ygd[6])/(rga-rs[6]))



def propiedades_standing (profundidad, celda, ti_cabeza, ti_fondo, presion_cabeza,qo,api,ygt,rga,rugosidadpendiente,constanteT):
    pass


def beggs():
    pass


if __name__ == "__main__":
    run ()
