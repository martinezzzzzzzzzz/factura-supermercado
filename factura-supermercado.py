import os
 
# Lista de productos disponibles
productos = {
    "Manzana": 1.50,
    "Pan": 2.00,
    "Leche": 3.20,
    "Arroz": 1.80,
    "Huevos": 2.50
}
 
# Carrito de compras
carrito = {}
 
def mostrar_productos():
    print("\nProductos disponibles:")
    for i, (producto, precio) in enumerate(productos.items(), start=1):
        print(f"{i}. {producto} - ${precio:.2f}")
 
def agregar_producto():
    mostrar_productos()
    try:
        opcion = int(input("Ingrese el número del producto que desea comprar (0 para finalizar): "))
        if opcion == 0:
            return False
        producto = list(productos.keys())[opcion - 1]
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
 
        if cantidad <= 0:
            print("Cantidad inválida.")
            return True
 
        if producto in carrito:
            carrito[producto] += cantidad
        else:
            carrito[producto] = cantidad
        print(f"{cantidad} x {producto} agregado al carrito.\n")
    except (ValueError, IndexError):
        print("Opción no válida.")
    return True
 
def mostrar_factura():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nFactura de Compra")
    print("----------------")
    total = 0
    for producto, cantidad in carrito.items():
        precio = productos[producto] * cantidad
        total += precio
        print(f"{producto}: {cantidad} x ${productos[producto]:.2f} = ${precio:.2f}")
    print("----------------")
    print(f"Total a pagar: ${total:.2f}\n")
 
def main():
    print("Bienvenido al Supermercado Virtual 🛒")
    while agregar_producto():
        pass
    if carrito:
        mostrar_factura()
    else:
        print("No se compraron productos.")
 
if __name__ == "__main__":
    main()