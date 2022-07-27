#!/usr/bin/python3
#Adminis_dos version 0.2
# Reestruturar administracion-2
from os import remove
import time
#from tkinter import filedialog
import tkinter as tk
import tkinter.font as tkFont
#from tkinter import ttk
#from tkinter import *
from modul import fundb,color_fun,cactur_to
from tkinter import filedialog
import os
#import tkinter as tk
import shutil


def renomb(dat):
    ficher = ""
    con = ".pdf"
    if dat != con:
        ficher = filedialog.askopenfilename(title="Abrir", initialdir="/home/manuel/", filetypes=(
            ("Fichros de texto", "*.pdf"), ("Ficheros de excel", "*.xlxs")))
        os.rename(ficher, dat)
        path, filename = os.path.split(ficher)
        wd = os.getcwd()
        wdc=wd+"/" + dat
        shutil.copy(wdc,path)
        #
        #shutil.copy(filename,wd)
        print('helo')
        return dat
    else:
        tk.messagebox.showinfo(
            'Informacion', 'Tienes que poner fecha en rename')
        return
class Aplicacion():
#-------- Inicia ventana -----------------------
    def __init__(self,master):
        self.fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        self.ventana= master
        self.DibujarVentana()
        self.ventana.resizable(0,0)
# ----- Limpia ventana -------------------------
    def clearText(self):
        self.text.delete("1.0", "end")
        return
    def DibujarVentana(self):
      ##  self.dia = time.strftime("%d-%m-%Y")
        self.variable = tk.StringVar()
        self.variable1 = tk.StringVar()
        self.data = {'aguafr': '1', 'aguali': '4', 'luz - ': '2', 'telefo': '3',
                ' aguaf': '1', ' agual': '4', ' luz -': '2', ' telef': '3'}

        self.OptionList = [
            "Menu ver",
            "Ver Todos",
            "aguafria",
            "agualiente",
            "luz",
            "telefono"]

        self.OptionList1 = [
            "Grabar",
            "aguafria",
            "agualiente",
            "luz",
            "telefono"]
# ---------- Menu elegir Proveedoe para editar
        self.variable.set(self.OptionList[0])
        self.labF = tk.LabelFrame(self.ventana, bg="red", text="                 Proveedores                             Rename                              Facturas                        ")
        self.labF.grid(column=0, row=0, pady=1, padx=1, sticky="we")
        self.opt = tk.OptionMenu(self.labF, self.variable, *self.OptionList)
        self.opt.config(width=12, fg='blue', font=('Helvetica', 10, "bold"))
        self.opt.grid(row=0, column=0, padx=50, sticky="wse")
        self.variable.trace("w",self.Opcion_ver)
#---------- Editor de fecha -----------------------
        self.txt_fe = tk.Entry(self.labF, width=17)
        self.txt_fe.config(background="#ccff66",foreground='#FD0114',justify='center')
        self.txt_fe.grid(row=0, column=2, sticky="ws")
       # self.txt_fe.insert(0,self.dia + '.pdf')
#-------- Menu de elegir Proveedor ---------------------
        self.variable1.set(self.OptionList1[0])
        self.opt1 = tk.OptionMenu(self.labF, self.variable1, *self.OptionList1)
        self.opt1.config(width=12, fg='blue', font=('Helvetica', 10, "bold"))
        self.opt1.grid(row=0, column=5, padx=50, sticky="wse")
        self.variable1.trace("w", self.GrabaFa)
#------- Editor de texto ------------------------
        self.text = tk.Text(self.ventana, width=60, height=18, font=self.fontExample )  ##font=('Arial', 13), background="white")
        self.text.grid(column=0, row=1)
        self.text.configure(yscrollcommand='pass') 
        self.vsb = tk.Scrollbar(command=self.text.yview, orient="vertical")
        self.vsb.grid(row=1, column=0, pady=1, sticky='nes')

# ---------------Graba una Factura de un Proveedor
    def GrabaFa(self,*args):
        var = self.variable1.get()
        if var == 'Grabar':
            pass
        else:
            self.pdftxt=renomb(self.txt_fe.get())
            self.fitxt=cactur_to.conver(self.pdftxt)
            dates = cactur_to.cacturar(self.fitxt, var)
            fundb.ingresa(dates)
#---------- Elige cuantos editar--------------------------
    def Opcion_ver(self,*args):
        var = self.variable.get()
        if var == 'Menu ver':
            pass
        elif var == 'Ver Todos':
            self.Ver_todos()
        else:
            self.Ve_uno()
            
#------ Muestra a todos los Proveedores --------
    def Ver_todos(self,*ags):
        no=""
        contenido = fundb.vertodo()
        self.clearText()
        self.text.config(state="normal")
        conte = color_fun.cuen(contenido)
        self.colorea(conte)
        tota=fundb.sumagastos(no)
        self.txt_fe.delete("0","end")
        self.txt_fe.insert(0,"Gasto Total "+ str(tota) )
        #self.text.insert("end","\n                          Gasto Total "+str(tota),"")
        remove("datos.txt")
#------- Muestra un Proveedor ------------------------
    def Ve_uno(self,*args):
        var = self.variable.get()
        contenido1 = fundb.verun(var)
        self.clearText()
        self.text.config(state="normal")
        conte = color_fun.cuen(contenido1)
        self.colorea(conte)
        tota=fundb.sumagastos(var)
        self.txt_fe.delete("0","end")
        self.text.insert("end","\n                              Gasto Total "+str(tota),"")
        remove("datos.txt")
# ---------- Colorea Proveedor -----------------------------
    def colorea(self,une):
        self.text.tag_configure("1", foreground="blue")
        self.text.tag_configure("2", foreground="red")
        self.text.tag_configure("4", foreground="green")
        self.text.tag_configure("3", background="black",foreground="white")
        f = open('datos.txt', 'w')
        for i in une:
            f.write(str(i))
        f.close()
        with open("datos.txt", "r") as f:
            for linea in f:
                prove = linea[4:10]
                self.text.insert("end", linea, self.data[prove])
        
        
#----- Arranca aplicacion -----------------------------
def main():
    root = tk.Tk()
    root.title("Administracion con clase")
    ancho_ventana = 630
    alto_ventana = 450
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    aplication=Aplicacion(root)
    root.mainloop()

if __name__ == '__main__':
    main()    
    
    
