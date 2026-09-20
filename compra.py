"""
Módulo de compra: calcula el total a partir de los productos en el carrito.
"""

def calcular_total(carrito):
    """
    Calcula y retorna el total sumando el precio de los productos del carrito.
    """
    if not carrito:
        return 0.0

    return sum(p["precio"] for p in carrito)
