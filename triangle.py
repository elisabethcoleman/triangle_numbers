#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:51:12 2020

@author: wednesday
"""

def trianlge_indirect(count):
    t = 1
    n = 1
    while n < count :
        print(int(t))
        n = n + 1
        t = t + n
        
def triangle_direct(count):
    n = 1
    t = 1
    while n < count: 
        print(int(t)) 
        n = n+1     
        t = n*(n+1)/2         
        
print("Triange Direct")
triangle_direct(25)
print(" ")
print("Triange Indirect")
trianlge_indirect(25)