# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:19:28 2020

@author: Omar
"""

pa = 0
d=float(input("Ingrese la distancia a recorrer: "))
v=int(input("Escoja un tipo de vuelo: Nacional(1) o Internacional(2) "))

while not(v==1) and not(v==2) :
    v=int(input("Ingrese un número válido "))

while pa<=337250 :
    p=float(input("Ingrese el peso del producto: "))
    if p>10 :
        pa=pa+p
        if pa<=355000 :   
            if v==1 :
                vd=4000*d
                vp=4500*p
                vt=vd+vp
                if p>100 :
                    vt=vt*0.85
            elif v==2:
                vd=8000*d
                vp=4500*p
                vt=vd+vp
                if pa>400 and d>8000 :
                    vt=vt*0.90
            print("El valor total es: " + str(vt))
        else : 
            print("El paquete supera el límite de peso")
            pa=pa-p
    else :
        print("El peso de su producto no es aceptado")
    d=float(input("Ingrese una nueva distancia: "))
    

    
            
            