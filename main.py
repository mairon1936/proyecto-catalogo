class Negocio:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def ver_catalogo(self):
        for producto in self.catalogo:
            print(f"{producto['nombre']}: ${producto['precio']}")

    def buscar_producto(self, nombre_buscado):
        nombre_buscado = str(nombre_buscado).strip().lower()
        for producto in self.catalogo:
            nombre_producto = str(producto.get("nombre", "")).strip().lower()
            if nombre_producto == nombre_buscado:
                return producto
        return None

    def agregar_productos(self, nombre, precio_texto, disponible):
        try:
            precio = float(precio_texto)
        except ValueError:
            print("el precio deve de ser un numero, producto no agregado")
            return None

        producto = {
            "nombre": nombre.strip(),
            "precio": precio,
            "disponivilidad": disponible
        }
        self.catalogo.append(producto)
        return producto

    def productos_disponibles(self):
        return [producto for producto in self.catalogo if producto["disponivilidad"]]


def menu(negocio):
    while True:
        print("\n--- Menú de productos ---")
        print("1. Ver catálogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un producto nuevo")
        print("4. Ver solo los productos disponibles")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            if not negocio.catalogo:
                print("El catálogo está vacío.")
                continue
            print("\nCatálogo completo:")
            negocio.ver_catalogo()

        elif opcion == "2":
            nombre_buscado = input("Introduce el nombre del producto: ").strip()
            if not nombre_buscado:
                print("Debes escribir un nombre válido.")
                continue
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

            precio_texto = input("Introduce el precio del producto: ")
            producto = negocio.agregar_productos(nombre, precio_texto, True)

            if producto is None:
                continue

            print("Producto agregado correctamente")

        elif opcion == "4":
            productos_en_stock = negocio.productos_disponibles()
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
    catalogo_negocio = [
        {"nombre": "masajes corporales", "precio": 500.00, "disponivilidad": True},
        {"nombre": "manicura", "precio": 200.00, "disponivilidad": True},
        {"nombre": "pedicura", "precio": 300.00, "disponivilidad": True}
    ]
    negocio = Negocio(catalogo_negocio)
    menu(negocio)


if __name__ == "__main__":
    main()
