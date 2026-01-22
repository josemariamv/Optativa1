#!/usr/bin/python3

import tkinter as tk
# from tkinter import messagebox

#Por terminar...

def hacer_clic(indice):
    def manejador_clic():
        # messagebox.showinfo("Información", "Has pulsado el botón " + str(indice))
        def hacer_movimiento(indice):
            """Maneja el clic en un botón del tablero."""
            global jugador
            if  botones[indice]["text"] == "":
                botones[indice]["text"] = jugador
                botones[indice].config(bg="yellow")
                if jugador == "X":
                    jugador = "O"
                else:
                    jugador = "X"
    return manejador_clic

# Variables globales para el estado del juego
botones = []
jugador = "X"

ventana = tk.Tk()
ventana.title("Tres en Raya")

for i in range(9):
    boton = tk.Button(ventana, font=("Arial", 36), height=3, width=5, bg="green", foreground="yellow", command=hacer_clic(i))
    fila = i // 3
    columna = i % 3
    boton.grid(row=fila, column=columna)
    botones.append(boton)

ventana.mainloop()