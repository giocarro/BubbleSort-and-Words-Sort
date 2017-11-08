#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Merge Sort Part 2

#a=[9,8,7,6,5]
#a=[8,7,6,9,1]
a=[0,9,1,4,6,7,2,1,8,7,7,4,3,5,6,1,7,8,0,3]
l=len(a) #20

li=l
x=0
while(li%2==0):
    li=li/2
    x=x+1

p=2**x
tamis=l/p #tamano intervalo inicial
inters=l/tamis #numero de intervalos
print 'Numero de intervalos=',inters,'\nTamano intervalo=',tamis,'\nLongitud de lista=',l,'\n',a

#li=len(a)
#g=0

#for t in range(x)
#for s in range(0,l,li*2**t):
s=0
g=1    
for h in range(s,l,tamis): #Ordenamiento todos los intervalos 
    for k in range(s,g*li-1): #ordenamiento g-esimo intervalo
        b=[]
        print 'b=',b,'\ng=',g
        n=0
        m=0
        for i in range(s,g*li-1): #variacion puntual
            for j in range(s,g*li): #variación puntual
                #print 'i=',i,'\nj=',j
                if i>=n: #Espacio donde me quede en la lista
                    if i<j: #Solo comparo con numeros de adelante
                        if a[i]<=a[j]: 
                            b.append(a[i])
                            n=j
                            if j==li-1: b.append(a[j]) #Cuando j llega a la ultima posicion y a[i]<a[j] entonces tambien añado a[j]
                            else: break
                        else:
                            b.append(a[j])
                            if j==li-1: 
                                m=m+1
                                b.append(a[i])
                                break
                else: break
            #print 'a= ',a,'\nb= ',b,'\nn=',n,'\ni=',i,'\n'
            if m>0: break
        a=[]
        a=list(b)
        print 'a= ',a,'\nb= ',b,'\nk=',k,'\ni=',i,'\nj=',j,'\nh=',h,'\ng*li-1=',g*li-1
    g=g+1
    s=s+li

