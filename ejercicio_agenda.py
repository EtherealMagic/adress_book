lista_contactos = {}
lista_nombres = []

while True:

    print("""
Bienvenid@ a su agenda.
1 - agregar un contacto.
2 - buscar un contacto.
3 - eliminar un contacto.
4 - ver lista de contactos.
5 - cerrar el programa.""")
    interfaz = input("ingrese una entrada: ")
    try:
        if interfaz == "1":
            nombre = input("nombre del nuevo usuario: ").capitalize()
            telefono = input("número de telefono: ")
            mail = input("mail del nuevo contacto: ")
            try:
                int(telefono)
                lista_contactos[nombre] = [telefono, mail]
                lista_nombres.append(nombre)
                print("contacto guardado con exito.")

            except ValueError:
                print("número invalido.")
            input("presione enter para volver.")

        elif interfaz == "2":
            entrada = input("nombre del contacto: ").capitalize()
            contacto = lista_contactos.get(entrada)
            if lista_contactos.get(entrada) == None:
                print("contacto no encontrado.")
                input("presione enter para volver.")
            else: 
                print(f"""
            nombre: {entrada}
            numero: {contacto[0]}
            mail: {contacto[1]}
            
""")
                input("presione enter para volver.")

        elif interfaz == "3":
            eliminado = input("contacto a eliminar: ").capitalize()
            if eliminado in lista_contactos:
                lista_contactos.pop(eliminado)
                lista_nombres.remove(eliminado)
                print("contacto eliminado con exito.")
            else:
                print("usuario no encontrado.")
                input("presione enter para volver.")

        elif interfaz == "4":
            print(f"""En tu lista de contactos se encuentran las siguientes personas: 
                  {lista_nombres}""")
            input("presione enter para volver.")
        elif interfaz == "5":
            break
    
    except:
        print("entrada invalida.")
