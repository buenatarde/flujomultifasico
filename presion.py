import numpy as np  
import matplotlib as plt
import pandas as pd

#from prueba import Bo


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

    qg = input("\n¿Cual es el gasto de gas en millones de pies cubicos por dia del pozo?:\t")
    assert qg.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    qg = float(qg)

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

    diametro = input("\n¿Cual es el diametro de la tuberia (en pulgadas)?:\t")
    assert diametro.replace(".","",1).isdigit(), "\n\nPor favor ingresa valores numericos"
    diametro = float(diametro)
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
    
    T = np.zeros(len(celdas))
    P = np.zeros(len(celdas))
#Comienza el programa MAIN
    errorexp=1
    while errorexp < error:
        for i in celdas:
            T[0]=ti_cabeza
            pass



def propiedades_vazquez (profundidad, celda, ti_cabeza, t,p,qo,api,ygt,rga,rugosidad,pendiente,constanteT):
    if api>30:
        C1 = 0.0178; C2 = 1.187; C3 = 23.931;
        Pb = (((rga*np.exp(-C3*(api/(t+460))))/(C1*ygt)))**(1/C2)
        ygd=np.zeros(6)
        ygd[0]=ygt
        rs=np.zeros(6)
        for i in range (1,6,1):
            #print("iteracion",i)
            rs[i] =ygd[i-1]*C1*(p**C2)*np.exp(C3*(api/(t+460)))
            #print("relacion solubilidad",rs)
            ygd[i] = .25+.02*api+((rs[i]*.000001)*(0.6874-(3.5864*api)))
            #print("densidad del gas disuleto",ygd)
        #print("valor de rs en posicion 5",rs[5])
        #print("valor de ygd en posicion 5",ygd[5])
        ygl = (((rga*ygt)-(rs[5]*ygd[5]))/(rga-rs[5]))
        #print("valor de ygl",ygl)
        C4 = .000467; C5 = .000011; C6 = .000000001377;
        Bo = 1+(C4*rs[5])+((t+460)*(api/ygd[5])*(C5+(C6*rs[5])))
        print("Factor volumetrico del aceite",Bo)


    else:
        C1 = 0.03062; C2 = 1.0937; C3 = 25.724;
        Pb = (((rga*np.exp(-C3*(api/(t+460))))/(C1*ygt)))*(1/C2)
        ygd=np.zeros(6)
        ygd[0]=ygt
        rs=np.zeros(6)
        for i in range (1,6,1):
            #print("iteracion",i)
            rs[i] =ygd[i-1]*C1*(p**C2)*np.exp(C3*(api/(t+460)))
            #print("relacion solubilidad",rs)
            ygd[i] = .25+.02*api+((rs[i]*.000001)*(0.6874-(3.5864*api)))
            #print("densidad del gas disuleto",ygd)
        #print("valor de rs en posicion 5",rs[5])
        #print("valor de ygd en posicion 5",ygd[5])
        ygl = (((rga*ygt)-(rs[5]*ygd[5]))/(rga-rs[5]))
        #print("valor de ygl",ygl)
        C4 = .000467; C5 = .000011; C6 = .000000001377;
        Bo = 1+(C4*rs[5])+((t+460)*(api/ygd[5])*(C5+(C6*rs[5])))
        print("Factor volumetrico del aceite",Bo)
    return(ygd[5],rs[5],Bo)


def propiedades_standing (profundidad, celda, ti_cabeza, t,p,qo,api,ygt,rga,rugosidad,pendiente,constanteT):
    Pb = 18.2*(((rga/ygt)**0.83)*(10**((.00091*t)-(0.0125*api)))-1.4)
    #print("\n\nPresion de burubuja por Stading",Pb)
    ygd = np.zeros(6)
    rs = np.zeros(6)
    ygd[0] = ygt
    for i in range (1,6,1):
        #print("iteracion",i)
        rs[i] =ygd[i-1]*((((p/18.2)+1.4)*(10**((.0125*api)-(.00091*t))))**(1/.83))
        #print("relacion solubilidad",rs)
        ygd[i] = .25+(.02*api)+((rs[i]*.000001)*(0.6874-(3.5864*api)))
        #print("densidad del gas disuleto",ygd)
    #print("valor de rs en posicion 5",rs[5])
    #print("valor de ygd en posicion 5",ygd[5])
    ygl = (((rga*ygt)-(rs[5]*ygd[5]))/(rga-rs[5]))
    #print("valor de ygl",ygl)
    yo=141.5/(api+131.5)
    Bo = .9759+.00012*((rs[5]*((ygd[5]/yo)**.5)+(1.25*t))**1.2)
    #print("Factor volumetrico del aceite",Bo)   
    return(ygd[5],rs[5],Bo)


def densidad_aceite(p,Pb,ygd,rs,Bo,yo,RGA,t,ygt,API):
    if p<Pb:
        densidad_aceite = ((yo*62.4)+(ygd*.0764*rs))/Bo
    else:
        densob = ((yo*62.4)+(ygd*.0764*RGA))/Bo
        Co = (-1.433+(5*RGA)+(17.2*t)-(1180*ygt)+(12.61*API))/(p*100000)
        densidad_aceite = densob*(np.exp(Co*(p-Pb)))
    sigmao = (42.4-(0.047*t)-(.267*API))*(np.exp(-0.0007*p))
    return(densidad_aceite,sigmao)


def viscosidades (p,Pb,rs,t,API):
    if p<Pb:
        x = (10**(3.0324-(.02023*API)))/(t**(1.163))
        viscod = (10**x)-1
        b = 5.44*((rs+150)**-.338)
        visco_aceite = (10.715*((rs+100)**-5.15))*(viscod**b)
    
    else:
        x = (10**(3.0324-(.02023*API)))/(t**(1.163))
        viscod = (10**x)-1
        b = 5.44*((rs+150)**-.338)
        visco_b = (10.715*((rs+100)**-5.15))*(viscod**b)
        a = (-3.9*.00001*p)-5
        m = 2.67*(p**1.187)*(10**a)
        visco_aceite = visco_b * ((p/Pb)**m)
    return (visco_aceite)


def propiedades_gas(t,p,ygl,):
    Tpc = 168+(325*ygl)-(12.5*ygl*ygl)
    Ppc = 677+(15*ygl)-(37.5*ygl*ygl)

    Tpr = t/Tpc
    Ppr = p/Ppc

    z = 1-((3.53*Ppr)/(10**(0.9813*Tpr))) + ((0.274*Ppr*Ppr)/(10**(0.8157*Tpr)))

    t_abs=t+459.67

    Bg = ((t_abs*z)/p)*.0282

    dens_g = (ygl*0.0764)/Bg

    x = 3.5 + (986/t_abs) + (0.2896*t_abs)
    y = 2.4-(0.2*x) 
    k = ((9.4+(0.5792*ygl))*(t**1.5))/((209+(550.24*ygl))+t_abs)
    visco_g = (k*.0001)*(np.exp(x*((dens_g/62.4)**y)))

    return(visco_g,Bg,dens_g)


def beggs(qg,diametro,rugosidad,t,p,qo,api,ygt,rga,pendiente,constanteT,densidad_aceite,sigmao):
    #Primeros paosos para determinar la velocidad superficial del liquido 
    diametro = diametro/12
    At = np.pi(1)*(diametro**2)*.25 #esto esta en pies cuadrados
    vsg = qg/At
    vsg = vsg/86400
    
    qo = qo*(5.615/86400)
    vsl = qo/At

    vm = vsl+vsg

    fracc_l = vsl/vm

    #Calculos para inicar con la correlacion
    L1 = 316*(fracc_l**0.302)
    L2 = 0.000925*(fracc_l**-2.468)
    L3 = 0.1*(fracc_l**-1.452)
    L4 = 0.5*(fracc_l**6.738)
    Nfr = (vm**2)/(diametro*32.2)

    #Determina
    if (fracc_l<0.01 and Nfr < L1) or (fracc_l >= 0.01 and Nfr<L2):
        patron_flujo = str("Segregado")

    elif (fracc_l >= 0.01 and L2 <= Nfr and Nfr <= L3):
        patron_flujo = str("Transicion")

    elif (0.01 <= fracc_l and fracc_l < 0.04 and L3 < Nfr and Nfr <= L1) or (fracc_l >= 0.4 and L3 < Nfr and Nfr <= L4):
        patron_flujo = str("Intermitente")

    elif (fracc_l < 0.4 and Nfr >= L1) or (fracc_l >= 0.4 and Nfr > L4):
        patron_flujo = str("Distribuido")
    else:
        print("Hubo un error en los datos favor de checarlos nuevamente")
    
    #Empieza la prediccion del Colgamiento

    if patron_flujo == "Segregado":
        a = 0.98; b = 0.4846; c = 0.0868
    elif patron_flujo == "Intermitente":
        a = 0.845; b = 0.5351; c = 0.0173
    elif patron_flujo == "Distribuido":
        a = 1.0659; b = 0.5824; c = 0.0609
    else: #Este es el de Transicion 
        a1 = 0.98; b1 = 0.4846; c1 = 0.0868; a2 = 0.845; b2 = 0.5351; c2 = 0.0173

    if patron_flujo == "Transicion":
        Hls = ((a1*(fracc_l**b1))/(Nfr**c1))
        Hli = ((a2*(fracc_l**b2))/(Nfr**c2))
    else:
        Hl = ((a*(fracc_l**b))/(Nfr**c))
    
    #Empieza los calculos para el Colgamiento

    if patron_flujo == "Segregado":
        e=0.011; f=-3.768; g=3.539; h=-1.614
    elif patron_flujo == "Intermitente":
        e=2.96; f=0.305; g=-0.4473; h=0.0978
    elif patron_flujo == "Distribuido":
        e=0.011; f=-3.768; g=3.539; h=-1.614
    else: #Este es el de Transicion
        es=0.011; fs=-3.768; gs=3.539; hs=-1.614
        ei=2.96; fi=0.305; gi=-0.4473; hi=0.0978
    
    Nlv = 1.938*vsl*((densidad_aceite/sigmao)**0.25)

    if patron_flujo == "Distribuido":
        C = 0; psi = 1
        Hl=Hl

    elif patron_flujo == "Transicion":
        Cs = (1-fracc_l)*np.ln(es*(fracc_l**fs)*(Nlv**gs)*(Nfr**hs))
        Ci = (1-fracc_l)*np.ln(ei*(fracc_l**fi)*(Nlv**gi)*(Nfr**hi))

        psis = 1 + Cs
        psii = 1 + Ci

        A = (L3-Nfr)/(L3-L4)

        Hls_psis = Hls*psis; Hli_psii = Hli*psii

        Hl = (A*Hls_psis) + ((1+A)*Hli_psii)

    else:
        C = (1-fracc_l)*np.ln(e*(fracc_l**f)*(Nlv**g)*(Nfr**h))
        psi = 1 + C

        Hl = Hl*psi

    #Calculo del Factor de Friccion

    ftp = 1



    
    




    


    



    




if __name__ == "__main__":
    run ()
