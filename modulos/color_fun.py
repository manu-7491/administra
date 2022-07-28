#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
import tkinter.font
import requests
import re
from itertools import islice

otro = ""
prove = []
lin = int(0)
cara = int(0)
tag = ""

def cuen(datu):
    palabras = ""
    palabras = datu.split()
    con = 0
    otro = ""
    n = ""
    coma = 0
    cu = int(palabras.__len__())
    for i in palabras:
        if i == str('('):
            n = n + ""
            con += 1
            coma = 1
            continue
            palabras = dat.split()
        elif i == "€":
            n = n + " "
        elif i == str(')'):
            n = n + '\n'
            con += 1
            continue
        elif i == ',' and coma == 3:
            n = n + ","
            coma = 0
            con += 1
        if i == ',':
            coma += 1
        elif i == "'":
            n = n + " - "
        else:
            n = n + i
            otro = otro + n
            n = ""
            con += 1
        if con == cu:
            break
        continue
    return(otro)
    
    
    f = open('datos.txt', 'w')
    for i in otro:
        f.write(str(i))
    f.close()

