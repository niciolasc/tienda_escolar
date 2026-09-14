"""
Tienda Escolar - Aplicativo de consola
Universidad Distrital Francisco José de Caldas
Programación Aplicada - Caso de estudio: Control de versiones

Permite registrar productos, calcular el total de una compra
y mostrar la información registrada.
"""

from productos import registrar_producto, mostrar_productos
from compra import calcular_total


def mostrar_menu():
    print("\n===== TIENDA ESCOLAR =====")
    print("1. Registrar producto")
    print("2. Mostrar productos registrados")
    print("3. Calcular total de compra")
    print("4. Salir")


def main():
    productos = []  # cada producto: {"nombre": str, "precio": float}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            calcular_total(productos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
