#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
POSITIVE_INFINITY = float("inf")

class Grafo:
    def __init__(self): 

        self.aristas = []   #lista
        self.vertices = {}  #diccionario
        
    def addVecinos(self,vertice1,vertice2):    
        self.addVertice(vertice1)
        self.addVertice(vertice2)
        self.vertices[vertice1].setVecino(vertice2)
        self.vertices[vertice2].setVecino(vertice1)
        arista = Arista(vertice1, vertice2)
        self.aristas.append(arista)

        
    def addVertice(self,nombre):
        if not self.vertices.has_key(nombre):
            vertice = Vertice(nombre)
            self.vertices[nombre] = vertice
    
    def cClustering(self):
        i = 0
        resultado = 0
        print("pensando...")
        for vertice in self.vertices.values():
            resultado += self.coefClustering(vertice.id)
            i += 1
        if (i > 0 ): return resultado/i
        return i
    
    def coefClustering(self,nombreVertice):
        nombreVecinos = self.vertices[nombreVertice].getVecinos()
        coef = 0
        
        for nombreVecino in nombreVecinos:
            nombreVecinos2 = self.vertices[nombreVecino].getVecinos()
            for nombreVecino2 in nombreVecinos2:
                if nombreVecino2 in nombreVecinos:
                    coef += 1
        n = len(nombreVecinos)
        maxRelaciones = n*(n-1)/2
        coef = coef/2 #debido a la forma de contar
                
        if ( maxRelaciones >0 ): return (coef/maxRelaciones)
        return 0         
    
    def caminoMinimo(self, nombrevertice1, nombreVertice2):
        nombreVecinos1 = self.vertices[nombrevertice1].getVecinos()
        nombreVecinos2 = self.vertices[nombreVertice2].getVecinos()
        
class Arista:
    def __init__(self, src, dst, weight=1):
        self.src = src
        self.dst = dst
        self.weight = weight

class Vertice:
    def __init__(self,node):
        self.id = node
        self.vecinos = []
        self.visitado = False
        self.distancia = POSITIVE_INFINITY
    
    def setVecino(self, vecino):
        self.vecinos.append(vecino)
        
    def getVecinos(self):
        return self.vecinos













#--------------------------------MAIN--------------------------------#
grafo = Grafo()
archivo = open("socfb-Caltech36.mtx")
#archivo = open("grafoprueba.txt")
texto = archivo.read().split()
i = 0
j = 1
while (i < len(texto) and j < len(texto)):
    vertice1 = texto[i]
    vertice2 = texto[j]
    grafo.addVecinos(vertice1, vertice2)
    i+= 2
    j+= 2
print("cantidad de vertices = " + str(len(grafo.vertices)))
print("cantidad de aristas = " + str(len(grafo.aristas)))
print("Coef. De Clustering Promedio = " + str(grafo.cClustering()))

archivo.close()