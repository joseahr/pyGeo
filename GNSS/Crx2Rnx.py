#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/2/2015

@author: Antonio Hermosilla Rodrigo.
@contact: anherro285@gmail.com
@organization: Antonio Hermosilla Rodrigo.
@copyright: (C) 2015 by Antonio Hermosilla Rodrigo
@version: 1.0.0
'''

from os.path import abspath,dirname,join,isfile
from re import search
from platform import system
from subprocess import Popen,PIPE


##print(platform.system())
##print(platform.release())
##print(platform.version())
def Crx2Rnx(RutaRINEXCompacto):
    '''
    El objeto de ésta función es recibir un fichero RINEX compacto y transformarlo
    en un fichero rinex standard.

    Para ello se utiliza la herramienta binaria crx2rnx.exe

    La función devuelve el fichero RINEX standard en la misma carpeta donde
    se encuentra el fichero RINEX compacto.

    @param Ruta_RINEX_compacto: Ruta del fichero RINEX compacto.
    @type Ruta_RINEX_compacto: string, list
    '''
    #Ruta de las herramientos binarias
    rutabin=abspath(join(dirname( __file__ ), '..', 'bin'))
    try:
        if "Linux" in system():
            exe=rutabin+'/Linux/CRX2RNX'
        elif "Windows" in system():
            exe=rutabin+'/Windows/crx2rnx'
    except Exception as e:
        raise Exception(e)
    #Comprobación del tipo de dato introducido:
    if type(RutaRINEXCompacto)==str:
        try:
            isfile(RutaRINEXCompacto)
            if RutaRINEXCompacto.endswith("d") or RutaRINEXCompacto.endswith("D") and search("\d\d",RutaRINEXCompacto.split(".")[1]):
                pass
            else:
                raise Exception("La extensión del archivo no es válida")
            try:
                p1 = Popen(exe+' -f '+'"'+RutaRINEXCompacto+'"', shell=True, stdout=PIPE, stderr=PIPE)
                outs, errs =p1.communicate()
                p1.poll()
                return outs
            except Exception as e:
                if p1.returncode==0:
                    return outs
                if p1.returncode == 1:
                    return errs
                if p1.returncode == 2:
                    return errs
        except Exception as e:
            raise Exception(e)
        
    elif type(RutaRINEXCompacto)==list:
        for i in RutaRINEXCompacto:
            print(i)
            if not type(i)==str:
                print("la ruta "+i+" no es de tipo str")
            else:
                try:
                    isfile(i)
                    if i.endswith("d") or i.endswith("D") and search("\d\d",i.split(".")[1]):
                        pass
                    else:
                        raise Exception("La extensión del archivo no es válida")
                    try:
                        p1 = Popen(exe+' -f '+'"'+i+'"', shell=True, stdout=PIPE, stderr=PIPE)
                        outs, errs =p1.communicate()
                        p1.poll()
                        #return outs
                    except Exception as e:
                        if p1.returncode==0:
                            return outs
                        if p1.returncode == 1:
                            return errs
                        if p1.returncode == 2:
                            return errs
                except Exception as e:
                    print(e)
                    continue
    else:
        raise Exception("La ruta no es de tipo str o list")



def main():
    rutasample=abspath(join(dirname( __file__ ),'..','ejemplos'))
    #Conversión Rinex Compacto a Rinex standard
    #rutaunion=rutasample+"/unionRinex"
    rutaunion=rutasample
    validos=[]
    from os import listdir
    for i in listdir(rutaunion):
        if 'DENI' in i and i.endswith('d'):
            validos.append(rutaunion+"/"+i)
    print(validos)
    Crx2Rnx(validos)

if __name__ == "__main__":
    main()
        