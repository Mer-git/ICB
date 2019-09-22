# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def largo (l, n):
    i=0
    cuenta=1
    valor1=0
    valor2=0
    while cuenta < n+1 or cuenta==n+1:
        a=l[i]
        b=l[i+1]
        if a==b:
            cuenta+= 1
            valor1=a
        i+=1
    cuenta=1
    while cuenta < n or cuenta == n and i<len(l)-1:
        c=l[i]
        d=l[i+1]
        if c==d:
            cuenta+= 1
            valor2=c
        i+=1
    alto=abs(valor1-valor2)
    return alto

def hayBorde(l,n,h):
    if largo(l,n)==h:
        return True
    else:
        return False

print(hayBorde([2,4,4,4,6,6,6,10,10],2,4))
