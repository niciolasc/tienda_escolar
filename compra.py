"""
Módulo de compra: calcula el total de una compra a partir de los
productos registrados.
"""


def calcular_total(productos):
    """Calcula y muestra el total de la compra sumando el precio de
    todos los productos registrados."""
    if not productos:
        print("No hay productos registrados para calcular el total.")
        return

    total = sum(p["precio"] for p in productos)
    print(f"\nTotal de la compra: ${total:.2f}")
    return total
