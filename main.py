catalogo_negocio = [
    {"nombre": "masajes corporales", "precio": 500.00, "disponivilidad": True},
    {"nombre": "manicura", "precio": 200.00, "disponivilidad": True},
    {"nombre": "pedicura", "precio": 300.00, "disponivilidad": False}
]


class Negocio:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def ver_catalogo(self):
        for producto in self.catalogo:
            print(f"{producto['nombre']}: ${producto['precio']}")

    def buscar_producto(self, nombre_buscado):
        nombre_buscado = nombre_buscado.strip().lower()
        for producto in self.catalogo:
            if producto["nombre"].lower() == nombre_buscado:
                return producto
        return None


def agregar_productos(catalogo, nombre, precio, disponible):
    producto = {
        "nombre": nombre.strip(),
        "precio": precio,
        "disponivilidad": disponible
    }
    catalogo.append(producto)


def productos_disponibles(catalogo):
    while True:
        print("\n--- Menú de productos ---")
        print("1. Ver catálogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un producto nuevo")
        print("4. Ver solo los productos disponibles")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            if not catalogo:
                print("El catálogo está vacío.")
                continue
            for producto in catalogo:
                print(f"{producto['nombre']}: ${producto['precio']}")

        elif opcion == "2":
            nombre_buscado = input("Introduce el nombre del producto: ").strip()
            if not nombre_buscado:
                print("Debes escribir un nombre válido.")
                continue
            negocio = Negocio(catalogo)
            producto = negocio.buscar_producto(nombre_buscado)
            if producto is not None:
                print(producto)
            else:
                print("Producto no encontrado")

        elif opcion == "3":
            nombre = input("Introduce el nombre del producto: ").strip()
            if not nombre:
                print("El nombre del producto no puede estar vacío.")
                continue

            try:
                precio = float(input("Introduce el precio del producto: "))
            except ValueError:
                print("El precio debe ser un número válido.")
                continue

            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue

            agregar_productos(catalogo, nombre, precio, True)
            print("Producto agregado correctamente")

        elif opcion == "4":
            productos_en_stock = [producto for producto in catalogo if producto["disponivilidad"]]
            if not productos_en_stock:
                print("No hay productos disponibles en este momento.")
                continue
            for producto in productos_en_stock:
                print(f"{producto['nombre']}: ${producto['precio']}")

        elif opcion == "0":
            print("Adiós")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


def main():
    productos_disponibles(catalogo_negocio)


if __name__ == "__main__":
    main()
