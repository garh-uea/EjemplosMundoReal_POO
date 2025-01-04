# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Cantidad: {self.cantidad}"

    def actualizar_stock(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            return True
        return False

# Clase Cliente
class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def realizar_compra(self, producto, cantidad):
        total = producto.precio * cantidad
        if self.saldo >= total:  # Primero se verifica si el cliente tiene saldo suficiente
            if producto.actualizar_stock(cantidad):  # Luego se actualiza el stock solo si la compra es posible
                self.saldo -= total
                print(f"Compra realizada con éxito! {self.nombre} compró {cantidad} {producto.nombre}.")
                print(f"Saldo restante: ${self.saldo}")
            else:
                print(f"No hay suficiente stock de {producto.nombre} para realizar la compra.")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para completar la compra.")

# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre}:")
        for producto in self.productos:
            print(producto)

    def realizar_venta(self, cliente, producto, cantidad):
        cliente.realizar_compra(producto, cantidad)

# Crear instancias de productos
producto1 = Producto("Camiseta", 20, 100)
producto2 = Producto("Pantalón", 30, 50)

# Crear una tienda y agregar productos
tienda = Tienda("Tienda de Ropa <<TENA STORE>>")
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Crear un cliente
cliente1 = Cliente("Gustavo Rodríguez", 80)
cliente2 = Cliente("María Cevallos", 60)

# Mostrar inventario

tienda.mostrar_inventario()

# Realizar compra de camisetas
tienda.realizar_venta(cliente1, producto1, 3)

# Realizar compra de pantalones
tienda.realizar_venta(cliente2, producto2, 2)

# Mostrar inventario después de la compra
tienda.mostrar_inventario()
