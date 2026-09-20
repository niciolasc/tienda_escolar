"""
Módulo de productos: gestión del inventario (catálogo) de la tienda escolar.
"""

# Memoria pre-cargada con productos
_inventario = [
    {"nombre": "Empanada", "precio": 2500.0},
    {"nombre": "Jugo Natural", "precio": 2000.0},
    {"nombre": "Paquete de Papas", "precio": 1800.0},
    {"nombre": "Sandwich", "precio": 3500.0},
    {"nombre": "Chocoramo", "precio": 2200.0}
]

def obtener_inventario():
    """Devuelve la lista actual de productos en el catálogo."""
    return _inventario

def registrar_producto_logica(nombre, precio_str):
    """
    Valida y agrega un nuevo producto al inventario.
    Lanza ValueError si los datos son inválidos.
    """
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre del producto no puede estar vacío.")

    try:
        precio = float(precio_str)
        if precio < 0:
            raise ValueError("El precio no puede ser un valor negativo.")
    except ValueError:
        raise ValueError("Ingrese un precio numérico válido.")

    _inventario.append({"nombre": nombre, "precio": precio})
