catalogo_negocio = [
    {"nombre": "masajes corporales", "precio": 500.00, "disponivilidad": True},
    {"nombre": "manicura", "precio": 200.00, "disponivilidad": True},
    {"nombre": "pedicura", "precio": 300.00, "disponivilidad": False}
]


def buscar_producto(catalogo, nombre_buscado):
    for producto in catalogo:
        if producto["nombre"] == nombre_buscado:
            return producto
    return None


def agregar_productos(catalogo, nombre, precio, disponible):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "disponivilidad": disponible
    }
    catalogo.append(producto)



def main():
    while True:
        print("1. Ver catálogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un producto nuevo")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            for producto in catalogo_negocio:
                print(f"{producto['nombre']}: ${producto['precio']}")

        if opcion == "2":
            nombre_buscado = input("Introduce el nombre del producto: ")
            producto = buscar_producto(catalogo_negocio, nombre_buscado)
            if producto is not None:
                print(producto)
            else:
                print("Producto no encontrado")

        if opcion == "3":
            nombre = input("Introduce el nombre del producto: ")
            precio = float(input("Introduce el precio del producto: "))
            agregar_productos(catalogo_negocio, nombre, precio, True)
            print("Producto agregado correctamente")

        if opcion == "0":
            print("Adiós")
            break


if __name__ == "__main__":
    main()
