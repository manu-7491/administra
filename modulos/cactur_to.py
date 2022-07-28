#!/usr/bin/python3
import os
# recupera total en numero
def cacturar(fich,prob):
    import sys
    import re
    from io import open
  
    s = []
    lin = []
    busca = "total"
    #diret=os.getcwd()
    diret=os.path.dirname(os.path.realpath(sys.argv[0]))
    if not os.path.isdir(diret + "/datbase"):
        os.makedirs(diret+"/datbase")
    #salida = diret + "/datbase/"administracion.db"
    #print(salida)
    archivo = fich
    obj = []
    obj2= []
    # guarda por palabra
    lineas = []
    datos2 = []
    num = 0
    cuen = 0
    cuent = 0
    fech=""
    fname=""
    #uno=""
    with open(archivo) as fname:
        fech = archivo[-18:-8]
        for lineas in fname:
            # convierte a minuscula
            lin = lineas.lower()
            num += 1
            if busca in lin:
                datos2 = lin
                # quita texto y deja numeros
                obj = re.sub(r'\D', "", datos2)
                cuent = num+1
                with open(archivo) as f:
                    for linea in f:
                        cuen += 1
                        if cuen == cuent:
                            # quita texto y deja numeros
                            obj2 = re.sub(r'\D', "", linea)
                            # pone la coma
                            if obj:
                                  s = obj[:-2] + ',' + obj[2:] + ' €'
                            else:
                                s = obj2[:-2] + ',' + obj2[2:] + ' €'
                            
                            #with open(salida, "a") as archivo_salida:
                                
                             #   lin = " - fecha - " + fech + "\n"
                               # uno = prob + " " + s + lin
                                #print(salida)
                               # archivo_salida.write(uno)
                                
                f.close()
    fname.close()
    os.remove(archivo)
    return(prob, s, fech)
    

# convierte pdf en txt
def conver(filepf):
    import fitz
    doc = []
    fname = ""
    fname = filepf  # sys.argv[1]  # get document filename
    doc = fitz.open(fname)  # open document
    out = open(fname + ".txt", "wb")  # open text output
    page = doc.loadPage(0)
    text = page.getText().encode("utf8")  # get plain text (is in UTF-8)
    out.write(text)  # write text of page
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
    out.close()
    os.remove(filepf)
    return (fname + ".txt")

   
