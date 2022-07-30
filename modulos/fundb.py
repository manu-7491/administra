#!/usr/bin/python3
# ------------------ crea base datos y crea table -------------------------------
import sys
import  sqlite3 
from tkinter import messagebox
from webbrowser import get
import os
#diret = os.getcwd()
diret = os.path.dirname(os.path.realpath(sys.argv[0]))
def conectar():
    if not os.path.isdir(diret + "/datbase"):
        os.makedirs(diret+"/datbase")
        #arch = open(diret+"/datbase/administracion.db",'a')
        #arch.close()
    miConexion=sqlite3.connect(diret+"/datbase/facturas.db")
    miCursor=miConexion.cursor()
    miCursor.execute ("CREATE TABLE IF NOT EXISTS  proveedores (ID INTEGER PRIMARY KEY AUTOINCREMENT,proveedor VARCHAR (20),total VARCHAR (20),fecha VARCHAR (20))" )
    miConexion.close()
    return
#------------------------------- inserta datos -------------------------   
def ingresa(na):
    #nam=[]
    nam=na
    #tota=tot
    #feche=fech
    conectar()
    #diret = os.getcwd()
    diret = os.path.dirname(os.path.realpath(sys.argv[0]))
    if not os.path.isdir(diret + "/datbase"):
        os.makedirs(diret+"/datbase")
    miConexion = sqlite3.connect(diret+"/datbase/facturas.db")
    miCursor = miConexion.cursor()
    argumentos=(nam)
    sql='''
    INSERT INTO proveedores(proveedor,total,fecha)
    VALUES(?,?,?)
    '''
    if (miCursor.execute(sql,argumentos)):
        messagebox.showinfo(message='Registro guardado con exito', title='Informacion')
    else:
        messagebox.showinfo(title='Informacion',message= 'Ha ocurrido un error al guardar el registro')
    miCursor.close()
    miConexion.commit()
    miConexion.close()
#------------------- saca todos ----------------------
def vertodo():
    todo = ""
    #diret = os.getcwd()
    diret = os.path.dirname(os.path.realpath(sys.argv[0]))
    if not os.path.isdir(diret + "/datbase"):
        os.makedirs(diret+"/datbase")
    conexion = sqlite3.connect(diret+"/datbase/facturas.db")
    consulta= conexion.cursor()
    if (conexion.cursor()):
        pass
        #tk.messagebox.showinfo('Informacion', 'Registro guardado con exito')
    else:
        messagebox.showinfo(title='Informacion', message='Ha ocurrido un error al guardar el registro')
    sql = "SELECT * FROM proveedores ORDER BY ID DESC"
    if(consulta.execute(sql)):
        tot = ""
        for tot in consulta:
            for sac in str(tot):
                todo = todo + str(sac)
                todo = todo + " "
            todo = todo + '\n'
    consulta.close()
    conexion.commit()
    conexion.close()
    return todo
#-------------- saca uno ---------------
def verun(tra):
    dates=[]
    un =str(tra)
    un ="'"+un+"'"
    #diret = os.getcwd()
    diret = os.path.dirname(os.path.realpath(sys.argv[0]))
    if not os.path.isdir(diret + "/datbase"):
        os.makedirs(diret+"/datbase")
    conexion = sqlite3.connect(diret+"/datbase/facturas.db")
    consulta = conexion.cursor()
    sql = "SELECT * FROM proveedores WHERE proveedor = "+un+" ORDER BY ID DESC;"
    consulta.execute(sql)
    filas= consulta.fetchall()
    tot = ""
    todo = ""
    for tot in filas:
        for sac in str(tot):
            todo = todo + str(sac)
            todo = todo + " "
        todo = todo + '\n'
    consulta.close()
    conexion.commit()
    conexion.close()
    return todo

def sumagastos(tra):
    uno =str(tra)
    uno ="'"+uno+"'"
    tod=float(0.0)
    diret = os.path.dirname(os.path.realpath(sys.argv[0]))
    if not os.path.isdir(diret + "/datbase"):
        os.makedirs(diret+"/datbase")
    conexion = sqlite3.connect(diret+"/datbase/facturas.db")
    consulta = conexion.cursor()
    if (conexion.cursor()):
        if (uno =="''"): 
            sql = "SELECT * FROM proveedores ORDER BY ID DESC"
        else:
            sql = "SELECT * FROM proveedores WHERE proveedor = "+uno+" ORDER BY ID DESC;"
        result = consulta.execute(sql)
    for row in result:
        cort=row[2]
        cort=cort.replace(",", ".")
        num= cort.replace("€", "")
        tod=float(tod)+float(num)
    consulta.close()
    conexion.commit()
    conexion.close()
    tod=round(tod,2)
    return (tod)






#if __name__ == "__main___":
#   verun()
#    conectar()