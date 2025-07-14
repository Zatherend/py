import time

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video,...]

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
 }

#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': ...
 }

while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    op = input("Seleccione una opción: ")

    if op == "1":
        marca = input("Ingrese la marca que desea consultar: ")
        existe = False
        for modelo in productos:
            if productos[modelo][0].lower() == marca.lower():
                print("Modelo:", modelo, "Stock:", stock.get(modelo, [0,0])[1])
                existe = True
        if not existe:
            print("No existe ningun producto de esa marca.")
        #stock = {modelo: [precio, stock], ...]
    if op == "2":
        precio_min = int(input("Precio mínimo: "))
        precio_max = int(input("Precio máximo: "))
        for modelo in productos:
            if modelo in stock:
                precio = stock[modelo][0]
                if precio_min <= precio <= precio_max and stock[modelo][1] > 0:
                    print("Los notebooks entre los precios consultas son:")
                    print(modelo)
    if op == "3":
        #stock = {modelo: [precio, stock], ...]
        modelo = input("Ingrese el modelo: ")
        if modelo in stock:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            stock[modelo][0] = nuevo_precio
            print("Precio actualizado.")
        else:
            print("El modelo no existe!!")
    if op == "4":
        print("Programa finalizado...")
        break
    else:
        print("Debe seleccionar una opción válida!!")
