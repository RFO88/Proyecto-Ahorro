from tkinter import *
import tkinter as tk
from tkinter import messagebox
import datetime

# Inicializar la lista de historial
historial = []


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simula tus ahorros")
ventana.geometry("700x650")
ventana.iconbitmap("img_pesos.ico")
ventana.config(bg="SkyBlue1")
ventana.resizable(1,1)


# Función para editar el nombre de una categoría de gasto
def editar_gasto(entry_field, label):
    nuevo_nombre = entry_field.get()  # Obtiene el nuevo nombre del campo de entrada
    if nuevo_nombre:
        label.config(text=f"Gastos en {nuevo_nombre}:")  # Actualiza la etiqueta
    else:
        messagebox.showerror("Error", "El nombre no puede estar vacío")
                

# Etiqueta y campo de entrada para ingresos
label_ingresos = tk.Label(ventana, text="INGRESOS MENSUALES:")
label_ingresos.grid(row=0, column=0, padx=10, pady=30)
entry_ingresos = tk.Entry(ventana)
entry_ingresos.grid(row=0, column=1, padx=10, pady=5)
label_ingresos.config(bg="SteelBlue3")

# Etiqueta y campo de entrada para gastos 1
label_gastos1 = tk.Label(ventana, text="Gastos 1:")
label_gastos1.grid(row=1, column=0, padx=10, pady=5)
entry_gastos1 = tk.Entry(ventana)
entry_gastos1.grid(row=1, column=1, padx=10, pady=5)
label_gastos1.config(bg="SlateGray1")

entry_gastos1_nombre = tk.Entry(ventana)
entry_gastos1_nombre.grid(row=1, column=2, padx=10, pady=5)
boton_editar_gastos1 = tk.Button(ventana, text="Editar tipo de gasto", command=lambda: editar_gasto(entry_gastos1_nombre, label_gastos1))
boton_editar_gastos1.grid(row=1, column=3, padx=10, pady=5)



# Etiqueta y campo de entrada para gastos 2
label_gastos2 = tk.Label(ventana, text="Gastos 2:")
label_gastos2.grid(row=2, column=0, padx=10, pady=5)
entry_gastos2 = tk.Entry(ventana)
entry_gastos2.grid(row=2, column=1, padx=10, pady=5)
label_gastos2.config(bg="SlateGray1")

entry_gastos2_nombre = tk.Entry(ventana)
entry_gastos2_nombre.grid(row=2, column=2, padx=10, pady=5)
boton_editar_gastos2 = tk.Button(ventana, text="Editar tipo de gasto", command=lambda: editar_gasto(entry_gastos2_nombre, label_gastos2))
boton_editar_gastos2.grid(row=2, column=3, padx=10, pady=5)

# Etiqueta y campo de entrada para gastos 3
label_gastos3 = tk.Label(ventana, text="Gastos 3:")
label_gastos3.grid(row=3, column=0, padx=10, pady=5)
entry_gastos3 = tk.Entry(ventana)
entry_gastos3.grid(row=3, column=1, padx=10, pady=5)
label_gastos3.config(bg="SlateGray1")

entry_gastos3_nombre = tk.Entry(ventana)
entry_gastos3_nombre.grid(row=3, column=2, padx=10, pady=5)
boton_editar_gastos3 = tk.Button(ventana, text="Editar tipo de gasto", command=lambda: editar_gasto(entry_gastos3_nombre, label_gastos3))
boton_editar_gastos3.grid(row=3, column=3, padx=10, pady=5)

# Etiqueta y campo de entrada para gastos 4
label_gastos4 = tk.Label(ventana, text="Gastos 4:")
label_gastos4.grid(row=4, column=0, padx=10, pady=5)
entry_gastos4 = tk.Entry(ventana)
entry_gastos4.grid(row=4, column=1, padx=10, pady=5)
label_gastos4.config(bg="SlateGray1")

entry_gastos4_nombre = tk.Entry(ventana)
entry_gastos4_nombre.grid(row=4, column=2, padx=10, pady=5)
boton_editar_gastos4 = tk.Button(ventana, text="Editar tipo de gasto", command=lambda: editar_gasto(entry_gastos4_nombre, label_gastos4))
boton_editar_gastos4.grid(row=4, column=3, padx=10, pady=5)

# Etiqueta y campo de entrada para gastos 5
label_gastos5 = tk.Label(ventana, text="Gastos 5:")
label_gastos5.grid(row=5, column=0, padx=10, pady=5)
entry_gastos5 = tk.Entry(ventana)
entry_gastos5.grid(row=5, column=1, padx=10, pady=5)
label_gastos5.config(bg="SlateGray1")

entry_gastos5_nombre = tk.Entry(ventana)
entry_gastos5_nombre.grid(row=5, column=2, padx=10, pady=5)
boton_editar_gastos5 = tk.Button(ventana, text="Editar tipo de gasto", command=lambda: editar_gasto(entry_gastos5_nombre, label_gastos5))
boton_editar_gastos5.grid(row=5, column=3, padx=10, pady=5)

# Etiqueta y campo de entrada para gastos 6
label_gastos6 = tk.Label(ventana, text="Gastos 6:")
label_gastos6.grid(row=6, column=0, padx=10, pady=5)
entry_gastos6 = tk.Entry(ventana)
entry_gastos6.grid(row=6, column=1, padx=10, pady=5)
label_gastos6.config(bg="SlateGray1")

entry_gastos6_nombre = tk.Entry(ventana)
entry_gastos6_nombre.grid(row=6, column=2, padx=10, pady=5)
boton_editar_gastos6 = tk.Button(ventana, text="Editar tipo de gasto", command=lambda: editar_gasto(entry_gastos6_nombre, label_gastos6))
boton_editar_gastos6.grid(row=6, column=3, padx=10, pady=5)





# Etiqueta y campo de entrada para la meta de ahorro
label_meta_ahorro = tk.Label(ventana, text="Objetivo de ahorro mensual:")
label_meta_ahorro.grid(row=7, column=0, padx=10, pady=5)
entry_meta_ahorro = tk.Entry(ventana)
entry_meta_ahorro.grid(row=7, column=1, padx=10, pady=5)


# Función para calcular el ahorro
def calcular_ahorro():
    try:
        ingresos = float(entry_ingresos.get())
        
        # Convertir las entradas de las categorías de gasto a valores numéricos
        gastos1 = float(entry_gastos1.get())
        gastos2 = float(entry_gastos2.get())
        gastos3 = float(entry_gastos3.get())
        gastos4 = float(entry_gastos4.get())
        gastos5 = float(entry_gastos5.get())
        gastos6 = float(entry_gastos6.get())
        
        # Sumar los gastos por categoría
        total_gastos = gastos1 + gastos2 + gastos3 + gastos4 + gastos5 + gastos6
        
        
        
        # Calcular el ahorro
        ahorro = ingresos - total_gastos
        
        # Verificar la meta de ahorro
        if entry_meta_ahorro.get():
            meta_ahorro = float(entry_meta_ahorro.get())
            
            if ahorro >= meta_ahorro:
                resultado.config(text=f'¡Felicidades! Has alcanzado tu objetivo de ahorro.\nAhorro: ${ahorro:.2f}')
            else:
                deficit = meta_ahorro - ahorro
                resultado.config(text=f'No has alcanzado tu objetivo . Te faltan: ${deficit:.2f}')
        else:
            if ahorro >= 0:
                resultado.config(text=f'Ahorro disponible: ${ahorro:.2f}')
            else:
                resultado.config(text=f'Tienes un déficit de: ${abs(ahorro):.2f}')
        

    except ValueError:
        messagebox.showerror('Error', 'Por favor, ingresa valores numéricos válidos')
        
# Botón para calcular el ahorro
boton_calcular = tk.Button(ventana, text="Calcular Ahorro", command=calcular_ahorro)
boton_calcular.grid(row=8, column=0, columnspan=2, pady=20)
boton_calcular.config(bg="gray71")


# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="", font=("Arial", 14))
resultado.grid(row=10, column=0, columnspan=2)
resultado.config(bg="SkyBlue1")

# Función para generar el reporte
def generar_reporte():
    try:
        ingresos = float(entry_ingresos.get())
        gastos1 = float(entry_gastos1.get())
        gastos2 = float(entry_gastos2.get())
        gastos3 = float(entry_gastos3.get())
        gastos4 = float(entry_gastos4.get())
        gastos5 = float(entry_gastos5.get())
        gastos6 = float(entry_gastos6.get())
        
        total_gastos = gastos1 + gastos2 + gastos3 + gastos4 + gastos5 + gastos6
        ahorro = ingresos - total_gastos
        
        meta_ahorro = 0
        if entry_meta_ahorro.get():
            meta_ahorro = float(entry_meta_ahorro.get())
        
# Verificar si ha alcanzado la meta
        if ahorro >= meta_ahorro:
            estado_meta = "Objetivo alcanzado"
            recomendacion= "Felicidades estas por buen camino!"
        else:
            estado_meta = f"Objetivo no alcanzado. Faltan: ${meta_ahorro - ahorro:.2f}"
            recomendacion= "Tienes que revisar tus gastos y reconsiderar\nalgunos si quieres alcanzar tu objetivo te recomendamos analizar gastos\ninnecesarios o calsificarlos por orden de prioridad"
        
# Calcular el porcentaje de ahorro
            porcentaje_ahorro = (ahorro / ingresos) * 100 if ingresos > 0 else 0

# Obtener la fecha actual
    
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")

# Guardar el reporte en el historial
        reporte = {
                "fecha": fecha_actual,
                "ingresos": ingresos,
                "gastos": total_gastos,
                "ahorro": ahorro,
                "meta_ahorro": meta_ahorro,
                "estado_meta": estado_meta,
                "recomendacion": recomendacion
            }
        historial.append(reporte)
            
# Generar el reporte
    # reporte_nombre=f"reporte_ahorro_{fecha_actual.replace('/', '-')}.txt"
        with open("reporte_ahorro.txt", "w") as file:
            file.write(f"--- Reporte del Ahorro ({fecha_actual}) ---\n")
            file.write(f"Ingresos: ${ingresos:.2f}\n")
            file.write(f"Gastos:\n")
            file.write(f"  - Gastos 1: ${gastos1:.2f}\n")
            file.write(f"  - Gastos 2: ${gastos2:.2f}\n")
            file.write(f"  - Gastos 3: ${gastos3:.2f}\n")
            file.write(f"  - Gastos 4: ${gastos4:.2f}\n")
            file.write(f"  - Gastos 5: ${gastos5:.2f}\n")
            file.write(f"  - Gastos 6: ${gastos6:.2f}\n")
            file.write(f"-----------------------------------------\n")          
            file.write(f"Total de Gastos: ${total_gastos:.2f}\n")
            file.write(f"Ahorro: ${ahorro:.2f}\n")
            file.write(f"Objetivo de Ahorro: ${meta_ahorro:.2f}\n") 
            file.write(f"Estado del Objetivo: {estado_meta}\n")
            file.write(f"-----------------------------------------\n")
            file.write(f"Recomendaciones: {recomendacion}\n")
            file.write(f"-----------------------------------------\n")
        
        messagebox.showinfo("Reporte Generado", "El reporte ha sido guardado como 'reporte_ahorro.txt'")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")

# Función para mostrar el historial de reportes
def mostrar_historial():
    if historial:
        historial_str = "\n".join([f"{r['fecha']}: Ahorro ${r['ahorro']:.2f}" for r in historial])
        messagebox.showinfo("Ahorro", f"Historial de Ahorros:\n{historial_str}")
    else:
        messagebox.showinfo("Ahorro", "No hay reportes en el historial.")


# Botón para generar el reporte
boton_reporte = tk.Button(ventana, text="Generar Reporte", command=generar_reporte)
boton_reporte.grid(row=11, column=0, columnspan=4, pady=10)
boton_reporte.config(bg="gray71")

# Botón para ver el historial de reportes
boton_historial = tk.Button(ventana, text="Mostrar Historial de Ahorro", command=mostrar_historial)
boton_historial.grid(row=12, column=0, columnspan=4, pady=10)


# Ejecutar la aplicación
ventana.mainloop()