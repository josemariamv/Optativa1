#!/usr/bin/python3
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

# python3 -m tkinter para ver la versión desde línea de comandos
# A partir de la 8.5 mejora sustancialmente
# multiplataforma windows-mac-linux

# Define la ventana principal de la aplicación
ventana = Tk()

# Define las dimensiones de la ventana, que se ubicará en
# el centro de la pantalla. Si se omite esta línea la
# ventana se adaptará a los widgets que se coloquen en
# ella.
ventana.geometry('600x480') # anchura x altura

# Asigna un color de fondo a la ventana. Si se omite
# esta línea el fondo será gris
ventana.configure(bg = 'beige')
ventana.configure(bg = '#00ff00')


# Asigna un título a la ventana
ventana.title('ASIR 1 :: Python')

# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón
ventana.boton = ttk.Button(ventana, text="Cerrar", command=quit)
ventana.boton.pack(side=BOTTOM)

# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de
# que alguna persona interactúe con ella.
ventana.mainloop()

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.