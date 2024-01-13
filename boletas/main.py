from tkinter import *

productos = {}

def añadirProducto(nombre, precio, cantidad):
    productos[nombre] = [float(precio), cantidad, float(precio) * float(cantidad)]
    actualizarInterfaz()

def eliminarProducto(nombre):
    if nombre in productos:
        del productos[nombre]
        actualizarInterfaz()
def resolver():
    total = 0
    for producto in productos.keys():
        total += productos[producto][2]
    return total

def actualizarInterfaz():
    # Limpiar la interfaz
    for widget in root.winfo_children():
        widget.destroy()

    # Crear la interfaz actualizada
    btnAñadirProducto = Button(root, text="Añadir producto", command=abrir_Producto, width=12, height=4)
    btnAñadirProducto.grid(row=0, column=0, padx=10, pady=10)

    nombre = Label(root, text="Nombre")
    nombre.grid(row=1, column=0, padx=10, pady=10)
    valor = Label(root, text="Valor")
    valor.grid(row=1, column=1, padx=10, pady=10)
    cantidad = Label(root, text="Cantidad")
    cantidad.grid(row=1, column=2, padx=10, pady=10)
    total = Label(root, text="Total")
    total.grid(row=1, column=3, padx=10, pady=10)
    row = 2
    for producto in productos.keys():
        label_nombre = Label(root, text=producto)
        label_nombre.grid(row=row, column=0, padx=10, pady=10)

        label_valor = Label(root, text=productos[producto][0])
        label_valor.grid(row=row, column=1, padx=10, pady=10)

        label_cantidad = Label(root, text=productos[producto][1])
        label_cantidad.grid(row=row, column=2, padx=10, pady=10)

        label_total = Label(root, text=productos[producto][2])
        label_total.grid(row=row, column=3, padx=10, pady=10)

        btn_eliminar = Button(root, text="eliminar", command=lambda: eliminarProducto(producto))
        btn_eliminar.grid(row=row, column=4, padx=10, pady=10)

        row += 1

    label_total = Label(root, text=f"Total: ${resolver()}")
    label_total.grid(row=row+1, column=0, padx=10, pady=10)

def abrir_Producto():
    formulario = Toplevel(root)
    formulario.title("Formulario")

    # Elementos del formulario
    etiqueta_nombre = Label(formulario, text="Nombre producto:")
    etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10)
    entrada_nombre = Entry(formulario)
    entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

    etiqueta_precio = Label(formulario, text="Precio:")
    etiqueta_precio.grid(row=1, column=0, padx=10, pady=10)
    entrada_precio = Entry(formulario)
    entrada_precio.grid(row=1, column=1, padx=10, pady=10)

    etiqueta_cantidad = Label(formulario, text="Cantidad:")
    etiqueta_cantidad.grid(row=2, column=0, padx=10, pady=10)
    entrada_cantidad = Entry(formulario)
    entrada_cantidad.grid(row=2, column=1, padx=10, pady=10)

    boton_guardar = Button(formulario, text="Guardar", command=lambda: añadirProducto(entrada_nombre.get(), entrada_precio.get(), entrada_cantidad.get()))
    boton_guardar.grid(row=3, column=0, columnspan=3, pady=10)

root = Tk()
root.title("Boletas de productos")
root.geometry("500x300")

# Inicializar la interfaz
actualizarInterfaz()

root.mainloop()
