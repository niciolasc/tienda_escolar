"""
Tienda Escolar - Interfaz Gráfica (GUI)
Universidad Distrital Francisco José de Caldas
Programación Aplicada - Caso de estudio
"""

import tkinter as tk
from tkinter import messagebox
from productos import obtener_inventario, registrar_producto_logica
from compra import calcular_total

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Escolar - Sistema de Ventas")
        self.root.geometry("650x450")
        
        # Memoria temporal de la compra actual
        self.carrito = []

        # --- PANEL SUPERIOR: REGISTRO ---
        frame_registro = tk.LabelFrame(self.root, text="Registrar Nuevo Producto al Inventario")
        frame_registro.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        tk.Label(frame_registro, text="Nombre:").pack(side=tk.LEFT, padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame_registro, width=20)
        self.entry_nombre.pack(side=tk.LEFT, padx=5)

        tk.Label(frame_registro, text="Precio: $").pack(side=tk.LEFT, padx=5)
        self.entry_precio = tk.Entry(frame_registro, width=15)
        self.entry_precio.pack(side=tk.LEFT, padx=5)

        btn_registrar = tk.Button(frame_registro, text="Guardar Producto", command=self.registrar)
        btn_registrar.pack(side=tk.LEFT, padx=15)

        # --- CONTENEDOR PRINCIPAL ---
        frame_principal = tk.Frame(self.root)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # PANEL IZQUIERDO: INVENTARIO
        frame_inv = tk.LabelFrame(frame_principal, text="Catálogo Disponible")
        frame_inv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.lista_inv = tk.Listbox(frame_inv)
        self.lista_inv.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        btn_agregar = tk.Button(frame_inv, text="Añadir al Carrito ->", command=self.agregar_carrito)
        btn_agregar.pack(pady=5)

        # PANEL DERECHO: CARRITO
        frame_car = tk.LabelFrame(frame_principal, text="Carrito de Compra")
        frame_car.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)

        self.lista_car = tk.Listbox(frame_car)
        self.lista_car.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.lbl_total = tk.Label(frame_car, text="Total: $0.00", font=("Arial", 12, "bold"))
        self.lbl_total.pack(pady=5)

        btn_limpiar = tk.Button(frame_car, text="Pagar / Vaciar Carrito", command=self.vaciar_carrito)
        btn_limpiar.pack(pady=5)

        # Inicializar listas en la interfaz
        self.actualizar_lista_inventario()

    def registrar(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        
        try:
            registrar_producto_logica(nombre, precio)
            messagebox.showinfo("Éxito", f"'{nombre}' añadido al catálogo.")
            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            self.actualizar_lista_inventario()
        except ValueError as e:
            messagebox.showerror("Error de Registro", str(e))

    def actualizar_lista_inventario(self):
        self.lista_inv.delete(0, tk.END)
        for p in obtener_inventario():
            self.lista_inv.insert(tk.END, f"{p['nombre']} - ${p['precio']:.2f}")

    def agregar_carrito(self):
        seleccion = self.lista_inv.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un producto del catálogo primero.")
            return
        
        # Recuperar el producto basado en el índice seleccionado
        index = seleccion[0]
        producto = obtener_inventario()[index]
        self.carrito.append(producto)
        
        self.actualizar_lista_carrito()

    def actualizar_lista_carrito(self):
        self.lista_car.delete(0, tk.END)
        for p in self.carrito:
            self.lista_car.insert(tk.END, f"{p['nombre']} - ${p['precio']:.2f}")
            
        total = calcular_total(self.carrito)
        self.lbl_total.config(text=f"Total: ${total:.2f}")

    def vaciar_carrito(self):
        if not self.carrito:
            return
        self.carrito.clear()
        self.actualizar_lista_carrito()
        messagebox.showinfo("Compra", "Transacción completada. Carrito vacío.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TiendaApp(root)
    root.mainloop()
