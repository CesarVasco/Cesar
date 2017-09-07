'''
Created on 20 de ago. de 2017

@author: cesar
'''
#Limpia la imagen 
def limpiar(sm,k,mIm,oIm):
    [smAlto, smAncho] = sm.shape
    smSize = k*k
    bcount = 0
    for x in range(0,smAlto):
        for y in range(0,smAncho):
            for s in range(0,smSize):
                if(s == 4 and sm[x][y][4] == 255):
                    bcount = bcount +1
                if sm[x][y][s] == 255 and s != 4:
                    bcount = bcount + 1
                        #print bcount
            if (bcount <= 3 and sm[x][y][4] == 255):
                mIm[x+1][y+1] = oIm[x][y]
            bcount = 0
    return mIm

def maxmin(oIm):
    [alto, ancho] = oIm.shape
    min = 255
    max = 0
    for x in range(0,alto):
        for y in range(0,ancho):
            valor = oIm[x][y]
            if( valor != 255 and valor > max):
                max = valor
            elif(valor != 255 and valor < min):
                min = valor
    return [max, min]

def reconocer(mIm,oIm):
    [maximo, minimo] = maxmin(oIm)
    #print "maximo:",maximo,"minimo",minimo
    [alto, ancho] = mIm.shape
    medio = (maximo-minimo)/3
    maximoMedio = maximo-medio
    minimoMedio = minimo+medio
    
    #Pinta las venas, el disco optico y la folvea no se que
    #print alto, " ", ancho
    for x in range(0,alto):
        for y in range(0,ancho):
            #if mIm[x,y] < 90 :    #(minimo + 50)    (maximo-60)
            if (maximoMedio-minimoMedio > 12 and oIm[x,y] < minimoMedio) or oIm[x,y]<70:
                #if (oIm[x,y] < minimoMedio and oIm[x,y] < maximoMedio):
                #if mIm[x,y] < minimoMedio and mIm[x,y] > 15:
                mIm[x,y] = 255
            if oIm[x][y] > 185 and oIm[x][y] < 255:
                mIm[x][y] = 0
    return mIm

"""
    #Reconocer viejo
    [maximo, minimo] = maxmin(oIm)
    print "maximo:",maximo,"minimo",minimo
    medio = (maximo+minimo)/2
    maximoMedio = maximo-medio*0.55
    minimoMedio = minimo+medio*0.55
    
    #Pinta las venas, el disco optico y la folvea no se que
    print alto, " ", ancho
    for x in range(0,alto):
        for y in range(0,ancho):
            #if mIm[x,y] < 90 :    #(minimo + 50)    (maximo-60)
            if mIm[x,y] < minimoMedio and mIm[x,y] < maximoMedio:
                mIm[x,y] = 255
            if mIm[x][y] > 190 and mIm[x][y] < 255:
                mIm[x][y] = 0
    """