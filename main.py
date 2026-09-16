catalogo_negocio = [
    {"nombre": "masajes corporales", "precio": 500.00, "disponivilidad": True},
    {"nombre": "manicura", "precio": 200.00, "disponivilidad": True},
    {"nombre": "pedicura", "precio": 300.00, "disponivilidad": False}
]



def main():
    while True:
        print("1. Ver catálogo completo")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            for producto in catalogo_negocio:
                print(f"{producto['nombre']}: ${producto['precio']}")

        if opcion == "0":
            print("Adiós")
            break


if __name__ == "__main__":
    main()
