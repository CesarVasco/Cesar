'''
Created on 5 de oct. de 2016

@author: cesar
'''
import numpy as np
from scipy import misc
import lpg
from Reconocer import limpiar, maxmin, reconocer
from multiprocessing import Process


    
if __name__ == '__main__':
    oIm = misc.imread('Images/MessidorBD/ojoModificado.tif', flatten=1)
    misc.imshow(oIm)
    mIm = oIm
    
    [alto,ancho] = oIm.shape
    
    k = 3
    cotaK = (k-1)/2
    blockSize = 120
    seccionAlto = (alto - (alto%blockSize))/blockSize
    seccionAncho = (ancho - (ancho%blockSize))/blockSize
    #print "secciones", seccionAlto,seccionAncho
    for seccionAl in range(0,seccionAlto):
        for seccionAn in range(0,seccionAncho):
            #print seccionAl, seccionAn
            mIm[seccionAl*blockSize:seccionAl*blockSize+blockSize,seccionAn*blockSize:seccionAn*blockSize+blockSize] = reconocer(mIm[seccionAl*blockSize:seccionAl*blockSize+blockSize,seccionAn*blockSize:seccionAn*blockSize+blockSize],oIm[seccionAl*blockSize:seccionAl*blockSize+blockSize,seccionAn*blockSize:seccionAn*blockSize+blockSize])
    #misc.imshow(mIm)
    #mIm = reconocer(mIm)
    
    
    #Se cargan las muestras para la limpieza
    sm = lpg.cargarTotalSamples(oIm, cotaK, k, alto, ancho)
    mIm = limpiar(sm,k,mIm,oIm)
    """
    [smAlto, smAncho] = sm.shape
    smSize = k*k
    bcount = 0
    for x in range(0,smAlto):
        for y in range(0,smAncho):
            for s in range(0,smSize):
                #if sm[x][y][4] > 190 and sm[x][y][4] < 255:
                #    mIm[x+1][y+1] = 0
                if(s == 4 and sm[x][y][4] == 255):
                    bcount = bcount +1
                if sm[x][y][s] == 255 and s != 4:
                    bcount = bcount + 1
                        #print bcount
            if (bcount <= 3 and sm[x][y][4] == 255):
                mIm[x+1][y+1] = oIm[x][y]
            bcount = 0
    """
    misc.imshow(mIm)
    misc.toimage(mIm, cmin=0, cmax=255).save('ojo3.tif')