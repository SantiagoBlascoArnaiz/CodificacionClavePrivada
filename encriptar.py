# -*- coding:utf-8 -*-
import sys
##########################################################################################
alphas = ['0000','0010','0100','1000',
          '0011','0110','1100','1011',
          '0101','1010','0111','1110',
          '1111','1101','1001','0001']

"""Suma realizada en el cuerpo de F16"""
def sumaCuerpo(vector,palabra):
    solucion = ''

    for i in range(len(vector)):
        if(vector[i]==palabra[i]):
            solucion = solucion + '0'
        else:
            solucion = solucion + '1'
    return solucion

"""Resta realizada en el cuerpo de F16"""
def restaCuerpo(vector,palabra):
    return(sumaCuerpo(vector,palabra))

"""Multiplicación realizada en el cuerpo de F16"""
def multCuerpo(vector,palabra):
    global alphas
    if(vector == alphas[0] or palabra == alphas[0]):
        solucion = 0
    else:
        solucion = (alphas.index(vector) + alphas.index(palabra)) % (len(alphas) - 1)
        if(solucion == 0):
            solucion = 15

    return alphas[solucion]

def invCuerpo(palabra):
    inv = 15 - alphas.index(palabra)
    if(inv == 0):
        inv = 15
    return alphas[inv]

##########################################################################################

"""Suma realizada en el cuerpo de F2"""
def sumaBinaria(num1,num2):
    if(num1 == num2):
        solucion = '0'
    else:
        solucion = '1'
    return solucion

"""Resta realizada en el cuerpo de F2"""
def restaBinaria(num1,num2):
    return(sumaBinaria(num1,num2))

"""Multiplicación realizada en el cuerpo de F2"""
def multBinaria(num1,num2):
    if(num1 == num2):
        solucion = num1
    else:
        solucion = '0'
    return solucion

##########################################################################################
def invString(palabra):
    invPalabra = ''
    
    for i in range(len(palabra)):
        invPalabra = invPalabra + palabra[len(palabra)-1-i]
    return invPalabra
def hexBin(numHex):
    hexa = {'0':'0000','1':'0001','2':'0010','3':'0011',
            '4':'0100','5':'0101','6':'0110','7':'0111',
            '8':'1000','9':'1001','a':'1010','b':'1011',
            'c':'1100','d':'1101','e':'1110','f':'1111'}
    return hexa[numHex]

def binHex(numBin):
    hexa = {'0000':'0','0001':'1','0010':'2','0011':'3',
            '0100':'4','0101':'5','0110':'6','0111':'7',
            '1000':'8','1001':'9','1010':'a','1011':'b',
            '1100':'c','1101':'d','1110':'e','1111':'f'}
    return hexa[numBin]

def matrizInferior(matriz,fila):
    inferior = []
    for i in range(len(matriz)):
        if(i != fila):
            filaInferior = []
            for j in range(len(matriz[i]) - 1):
                filaInferior.append(matriz[i][j])
            inferior.append(filaInferior)
    return inferior

def matHexBin(matriz):
    cambiada = []
    for fila in matriz:
        filaCambiada = []
        for elem in fila:
            filaCambiada.append(hexBin(elem))
        cambiada.append(filaCambiada)
    return cambiada
            
def determinanteCuerpo(matriz):
    if(len(matriz) == 2):
        return restaCuerpo(multCuerpo(matriz[0][0],matriz[1][1]),multCuerpo(matriz[0][1],matriz[1][0]))
    else:
        det = '0000'
        for i in range(len(matriz)):
            det = sumaCuerpo(det,multCuerpo(matriz[i][len(matriz)-1],determinanteCuerpo(matrizInferior(matriz,i))))
        return det
    
def determinanteBinario(matriz):

    if(len(matriz) == 2):
        return restaBinaria(multBinaria(matriz[0][0],matriz[1][1]),multBinaria(matriz[0][1],matriz[1][0]))
    else:
        det = '0'
        for i in range(len(matriz)):
            det = sumaBinaria(det,multBinaria(matriz[i][len(matriz)-1],determinanteBinario(matrizInferior(matriz,i))))
        return det

def printMat(mat):

    for i in range(len(mat)):
        print()
        for j in range(len(mat[i])):
            print(mat[i][j],end=' ')
    print()

def cadenaMat(cadena):
    mat = [[],[],[],[]]
    
    for i in range(4):
        for j in range(4):
            mat[j].append(cadena[i*4 + j])
    return mat

def cadenaMatCuerpo(cadena):
    mat = [[],[],[],[]]
    
    for i in range(4):
        for j in range(4):
            mat[j].append(hexBin(cadena[i*4 + j]))
    return mat

def matCadena(matriz):
    cadena=''
    for i in range(4):
        for j in range(4):
            cadena = cadena + matriz[j][i]
    return cadena

def matCadenaCuerpo(matriz):
    cadena=''
    for i in range(4):
        for j in range(4):
            cadena = cadena + binHex(matriz[j][i])
    return cadena

def cadenaVec(cadena):
    vec = []
    for i in cadena:
        vec.append(i)
    return vec

def vecCadena(vec):  
    cadena = ''
    for i in vec:
        cadena = cadena + i
    return cadena

def claveValida():
    valida = False
    matriz1 = cadenaMat(hexBin(clave[0])+hexBin(clave[1])+hexBin(clave[2])+hexBin(clave[3]))
    
    matriz2 = cadenaMat(hexBin(clave[5])+hexBin(clave[6])+hexBin(clave[7])+hexBin(clave[8]))
    
    suma1 = sumaCuerpo('0001', hexBin(clave[10]))
    suma1 = sumaCuerpo(suma1, hexBin(clave[11]))
    suma1 = sumaCuerpo(suma1, hexBin(clave[12]))
    
    suma2 = sumaCuerpo('0001', hexBin(clave[13]))
    suma2 = sumaCuerpo(suma2, hexBin(clave[14]))
    suma2 = sumaCuerpo(suma2,hexBin(clave[15]))
    
    if (determinanteBinario(matriz1) != '0' and determinanteBinario(matriz2) != '0' and suma1 != '0000' and suma2 != '0000'):
        valida = True
    
    return valida

def multMatBin(mat1,mat2):
    matRes = []
    
    for x in range(len(mat1)):
        matRes.append([])
        for _ in range(len(mat2[0])):
            matRes[x].append('0')
            
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                if(k == 0):
                    matRes[i][j] = multBinaria(mat1[i][k],mat2[k][j])
                else:
                    matRes[i][j] = sumaBinaria(matRes[i][j],multBinaria(mat1[i][k],mat2[k][j]))
    if(len(matRes[0]) == 1):
        temp = []
        for i in range(len(matRes)):
            temp.append(matRes[i][0])
        matRes = temp
    return matRes

def multMatCuerpo(mat1,mat2):
    matRes = []
    
    for x in range(len(mat1)):
        matRes.append([])
        for _ in range(len(mat2[0])):
            matRes[x].append('0000')
            
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                if(k == 0):
                    matRes[i][j] = multCuerpo(mat1[i][k],mat2[k][j])
                else:
                    matRes[i][j] = sumaCuerpo(matRes[i][j],multCuerpo(mat1[i][k],mat2[k][j]))
    if(len(matRes[0]) == 1):
        temp = []
        for i in range(len(matRes)):
            temp.append(matRes[i][0])
        matRes = temp
    return matRes

def sumaVecBin(vec1,vec2):
    for i in range(len(vec1)):
        vec1[i]=sumaBinaria(vec1[i], vec2[i])
    return vec1

def biyeccion0():
    cadenaSub = ''
    
    matriz = cadenaMat(invString(hexBin(clave[0]))+invString(hexBin(clave[1]))+invString(hexBin(clave[2]))+invString(hexBin(clave[3])))
    afin = cadenaVec(invString(hexBin(clave[4])))
    for letra in cadenaHex:
        letraVec = multMatBin(matriz,cadenaVec(invString(hexBin(letra))))
        letraVec = sumaVecBin(letraVec,afin)
        cadenaSub = cadenaSub + binHex(invString(vecCadena(letraVec)))
    return cadenaSub
    
def biyeccion1():
    cadenaSub = ''
    
    matriz = cadenaMat(invString(hexBin(clave[5]))+invString(hexBin(clave[6]))+invString(hexBin(clave[7]))+invString(hexBin(clave[8])))
    afin = cadenaVec(invString(hexBin(clave[9])))
    for letra in cadenaHex:
        letraVec = multMatBin(matriz,cadenaVec(invString(hexBin(letra))))
        letraVec = sumaVecBin(letraVec,afin)
        cadenaSub = cadenaSub + binHex(invString(vecCadena(letraVec)))
    return cadenaSub

def comprobarTxt(fichero):
    longitud = len(fichero)
    terminacion = fichero[(longitud - 4):longitud]
    if (terminacion != '.txt'):
        fichero = fichero + '.txt'
    return fichero

##############################################################################

def subElements(cadena,ronda):
    cadenaSub = ''
    if(ronda==0):
        for i in cadena:
            cadenaSub = cadenaSub + biy0[i]
    else:
        for i in cadena:
            cadenaSub = cadenaSub + biy1[i]
    return cadenaSub

def permutaFilas(cadena):
    matriz = cadenaMat(cadena)
    
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    for i in range(4):
        for j in range(4):
            pos = (j+i)%4
            mat[i][j] = matriz[i][pos]
    mat = matCadena(mat)
    return mat

def mixColumns(cadena,ronda):
    if(ronda==0):
        matriz = [[hexBin(clave[12]),'0001',hexBin(clave[10]),hexBin(clave[11])],
                  [hexBin(clave[11]),hexBin(clave[12]),'0001',hexBin(clave[10])],
                  [hexBin(clave[10]),hexBin(clave[11]),hexBin(clave[12]),'0001'],
                  ['0001',hexBin(clave[10]),hexBin(clave[11]),hexBin(clave[12])]]
    else:
        matriz = [[hexBin(clave[15]),'0001',hexBin(clave[13]),hexBin(clave[14])],
                  [hexBin(clave[14]),hexBin(clave[15]),'0001',hexBin(clave[13])],
                  [hexBin(clave[13]),hexBin(clave[14]),hexBin(clave[15]),'0001'],
                  ['0001',hexBin(clave[13]),hexBin(clave[14]),hexBin(clave[15])]]
    
    vectores = multMatCuerpo(matriz, cadenaMatCuerpo(cadena))

    return matCadenaCuerpo(vectores)

def sumaClave(cadena):
    cadenaResult = ''
    for i in range(len(cadena)):
        cadenaResult = cadenaResult + (binHex(sumaCuerpo(hexBin(clave[i]), hexBin(cadena[i]))))
    return cadenaResult

def encripta(cadena):
    cadEnc = subElements(cadena, 0)
    #print(cadEnc,'sub')
    cadEnc = permutaFilas(cadEnc)
    #print(cadEnc,'permuta')
    cadEnc = mixColumns(cadEnc, 0)
    #print(cadEnc,'mix')
    cadEnc = sumaClave(cadEnc)
    #print(cadEnc,'suma')
    
    #print()
    
    cadEnc = subElements(cadEnc, 1)
    #print(cadEnc,'sub')
    cadEnc = permutaFilas(cadEnc)
    #print(cadEnc,'permuta')
    cadEnc = mixColumns(cadEnc, 1)
    #print(cadEnc,'mix')
    #print()
    
    return cadEnc
    
if __name__ == "__main__":
    
    clave = str(input("Escriba una clave por favor: "))
    if (len(clave) != 16):
        print(clave, 'clave no valida')
        sys.exit()
    if not(claveValida()):
        print(clave, 'clave no valida')
        sys.exit()
    print(clave,'clave valida.')
    
    lectura = str(input("Escriba el nombre del fichero de lectura: "))
    escritura = str(input("Escriba el nombre del fichero de escritura: "))
    
    dirFicLec = comprobarTxt(lectura)
    
    ficheroVal = open(dirFicLec)
    valido = ficheroVal.read()
    ficheroVal.close()
    
    if(len(valido)%16 != 0):
        print('El fichero no contiene un número de letras múltiplo de 16.')
        sys.exit()
    
    cadenaHex = '0123456789abcdef'
    biy0 = dict(zip(cadenaHex,biyeccion0()))
    biy1 = dict(zip(cadenaHex,biyeccion1()))
    ficheroLec = open(dirFicLec)

    dirFicEsc = comprobarTxt(escritura)
    ficheroEsc = open(dirFicEsc, 'w')
    while True:
        cadena = ficheroLec.read(16)
        
        if not cadena:
            break
        
        cadena = encripta(cadena)
        ficheroEsc.write(cadena)
    ficheroLec.close()
    ficheroEsc.close()
    print('->Fin<-')