'''
Created on 20 de ago. de 2017

@author: cesar
'''
import numpy as np
from scipy import misc

#Se carga la matriz de vectores que contiene todas las muestras de la imagen
def cargarTotalSamples(im,cotaK,K,alto,ancho):
    #Nuevas dimensiones
    nAlto = alto - 2*cotaK
    nAncho = ancho - 2*cotaK
    sampleMatrix = np.zeros(shape=(nAlto,nAncho),dtype=object)
    sampleVector = np.zeros((K,K))
    [alto,ancho] = sampleMatrix.shape
    #Se fijan las cotas finales a partir de las nuevas dimensiones
    finAncho = ancho+cotaK
    finAlto = alto+cotaK
    for m in range(cotaK,finAlto):
        for n in range(cotaK,finAncho):
            #Se convierte a un array esta region de la imagen
            sampleVector = np.array(im[m-cotaK:m+cotaK+1,n-cotaK:n+cotaK+1]).reshape(K**2)
            sampleMatrix[m-cotaK][n-cotaK] = sampleVector
    return sampleMatrix

#Se carga la matriz de samples correspondiente a un pixel
def cargarSamples(sm,K,KK,L,x,y,cotaK,cotaL,alto,ancho,cantSamples,T):
    #Se atiende que no se sobrepasen los limites de la imagen
    infx = max(x-cotaL+cotaK,0)
    supx = min(alto,x+cotaL-cotaK+1)
    infy = max(y-cotaL+cotaK,0)
    supy = min(ancho,y+cotaL-cotaK+1)
    #Se crea la matriz de muestras en base a la cantidad maxima de muestras posibles
    samples = np.zeros(shape=(KK,cantSamples))
    col = 0
    cent = 0
    
    for m in range(infx,supx):
        for n in range(infy,supy):
            #Se calcula la distancia cuadratica
            emc = np.sum((sm[x][y]-sm[m][n])**2)
            emc = emc/KK
            #Se verifica si se cumple la condicion para agregar a la matriz de muestras
            if emc < T:
                #Se determina si se trata de la muestra a limpiar para saber su posicion en la matriz
                if m == x and n == y:
                    cent = col
                #Se carga por columna
                samples[0:KK,col] = sm[m][n]
                col += 1
    #Se eliminan las columnas que contienen 0s
    return (samples[:,0:col],cent,col)


def cargarSamples1(sm,K,KK,L,x,y,cotaK,cotaL,alto,ancho,cantSamples,T):
    #Se atiende que no se sobrepasen los limites de la imagen
    infx = max(x-cotaL+cotaK,0)
    supx = min(alto,x+cotaL-cotaK+1)
    infy = max(y-cotaL+cotaK,0)
    supy = min(ancho,y+cotaL-cotaK+1)
    #Se crea la matriz de muestras en base a la cantidad maxima de muestras posibles mas una fila para el emc
    samples = np.zeros(shape=(KK+1,cantSamples))
    col = 0
    
    for m in range(infx,supx):
        for n in range(infy,supy):
            #Se calcula la distancia cuadratica
            emc = np.sum((sm[x][y]-sm[m][n])**2)
            emc = emc/KK
            #Se verifica si se cumple la condicion para agregar a la matriz de muestras
            if emc < T:
                #Se carga por columna
                samples[0:KK,col] = sm[m][n]  
                #Se carga su emc correspondiente            
                samples[KK,col] = emc
                col += 1
    samples = samples[:,0:col]
    #Cantidad de muestras seleccionadas
    c = 15*25
    if col > c:
        return (samples[0:KK,0:c],0,c)
    #Se eliminan las columnas que contienen 0s
    return (samples[0:KK,0:col],0,col)