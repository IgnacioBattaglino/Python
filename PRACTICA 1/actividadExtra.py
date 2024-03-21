menu= "5"
inventory= {}
while menu != 4:
    menu= input (""" Elija una de las siguientes opciones:
           [1] Agregar un producto al inventario.
           [2] Eliminar un producto exitente del inventario.
           [3] Mostrar el inventario actual.
           [4] Salir del programa.
           """)
    if menu=="1":
        pname = input ("Ingrese el nombre del producto.")
        pcant = input ("Ingrese la cantidad de unidades.")
        inventory[pname]=pcant
