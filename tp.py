#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
POSITIVE_INFINITY = float("inf")
import matplotlib
import matplotlib.pyplot as plt
import time
class Grafo:
    def __init__(self): 

        self.aristas = []   #lista
        self.vertices = {}  #diccionario
        self.matAdy = []
        self.fdg = []

    def getVertices(self):
    	return self.vertices

    def crearMatAdy(self):
        maximo = 0
    	for arista in self.aristas:
    		src = int(arista.getSurce())
    		dst = int(arista.getDestiny())
    		if src >= dst:
    			maximo_aux = src
    		else: 
    			maximo_aux = dst
    		if maximo < maximo_aux:
    			maximo = maximo_aux
    	mat = []
    	for i in range(maximo+1):
    		fila = []
    		for j in range(maximo+1):
    			fila.append(0)
    		mat.append(fila)
    	for arista in self.aristas:
    		src = int(arista.getSurce())
    		dst = int(arista.getDestiny())
    		mat[src][dst] = 1
    		mat[dst][src] = 1
    	self.matAdy = mat
    	return mat

    def funcionDeGrado (self):
    	n = len(self.vertices.keys())	
    	for i in range(n):
    		self.fdg.append(0)
        resultado = 0
        n = 0
        for vert in self.vertices.keys():
            vertice = self.vertices[vert]
            cant = len(vertice.getVecinos())
            self.fdg[cant] = self.fdg[cant] + 1
            resultado += cant
            n += 1
    	return resultado/n

    def darFDG(self):
    	return self.fdg

    def printMat(self):
    	for fila in self.matAdy:
    		print fila

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
    
    def caminoMinimo(self, origen, destino):
        distancia = 0       
        if (origen == destino): return distancia
        
        distancia += 1
        nuevaLista = []
        visitados = []
        visitados.append(origen)
        vecinos = self.vertices[origen].getVecinos()

    
        while (distancia < len(self.vertices)) and (len(vecinos) > 0):
            if (destino in vecinos): return distancia
            for vecino in vecinos:
                if vecino not in visitados:
                    visitados.append(vecino)
                    for vecinoDeVecino in self.vertices[vecino].vecinos:
                        if vecinoDeVecino not in visitados:
                            nuevaLista.append(vecinoDeVecino)

            distancia += 1
            vecinos = nuevaLista
            nuevaLista = []

        return POSITIVE_INFINITY
    
    def caminoMinimoPromedio(self):
        i = 0
        resultado = 0
        visitados = []
        n = len(self.vertices.values())
        mat = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(0)
            mat.append(fila)
        print("pensando mucho...")
        i = 0
        for v1 in self.vertices.values():
            j = 0
            for v2 in self.vertices.values():
                nombrev1 = v1.id
                nombrev2 = v2.id
                if str(nombrev1)+","+str(nombrev2) not in visitados and str(nombrev2)+","+str(nombrev1) not in visitados and nombrev1 != nombrev2:
                    #print("busco " +str(nombrev1)+","+str(nombrev2) + "voy por el: " + str(i) )
                    res = self.caminoMinimo(nombrev1,nombrev2)
                    print mat
                    print j
                    print i
                    mat[i][j]= res
                    mat[j][i]= res
                    visitados.append(str(nombrev1)+","+str(nombrev2))
                j+=1
            i+=1    
        resultado = 0
        for i in range(n):
            for j in range(n):
                resultado += mat[i][j]
        if (resultado == 0): 
            return resultado
        else: 
            denom = n * (n-1)
            return resultado/denom
        
class Arista:
    def __init__(self, src, dst, weight=1):
        self.src = src
        self.dst = dst
        self.weight = weight

    def getDestiny(self):
    	return self.dst
    
    def getSurce(self):
    	return self.src

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
#archivo = open("socfb-Caltech36.mtx")
archivo = open("grafoprueba.txt")
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
print("Camino Minimo Promedio = " +str(grafo.caminoMinimoPromedio()))
#print(len(grafo.crearMatAdy()))
#grafo.printMat()

#print("Distribución de grado promedio = " + str(grafo.funcionDeGrado()))
#y = grafo.darFDG()
# n = len(grafo.getVertices().keys())	
# x = range(n)

# print len(y)
# print len(x)
# plt.plot(x, y)
# plt.show()
archivo.close()
