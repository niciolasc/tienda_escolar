"""
Módulo de productos: registrar y mostrar productos de la tienda escolar.
"""


def registrar_producto(productos):
    """Solicita al usuario el nombre y precio de un producto y lo agrega
    a la lista de productos registrados."""
    nombre = input("Nombre del producto: ").strip()

    while True:
        precio_str = input(f"Precio de '{nombre}': ").strip()
        try:
            precio = float(precio_str)
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Ingrese un precio válido (número).")

    productos.append({"nombre": nombre, "precio": precio})
    print(f"Producto '{nombre}' registrado con éxito.")


def mostrar_productos(productos):
    """Muestra en consola todos los productos registrados."""
    if not productos:
        print("No hay productos registrados todavía.")
        return

    print("\n--- Productos registrados ---")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")
