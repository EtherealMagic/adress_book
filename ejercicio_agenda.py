lista_contactos = {}
lista_nombres = []

while True:

    print("""
Bienvenid@ a su agenda.
1 - agregar un contacto.
2 - buscar un contacto.
3 - eliminar un contacto.
4 - ver lista de contactos.
5 - modificar un contacto.
6 - cerrar el programa.
""")
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
                input("""
contacto guardado con exito. Presione enter para volver.
""")

            except ValueError:
                print("número invalido.")
                input("""
presione enter para volver.
""")

        elif interfaz == "2":
            entrada = input("nombre del contacto: ").capitalize()
            contacto = lista_contactos.get(entrada)
            if lista_contactos.get(entrada) == None:
                print("contacto no encontrado.")
                input("""
presione enter para volver.
""")

            else: 
                print(f"""
            nombre: {entrada}
            numero: {contacto[0]}
            mail: {contacto[1]}
            
""")
                input("""
presione enter para volver.
""")

        elif interfaz == "3":
            eliminado = input("contacto a eliminar: ").capitalize()
            if eliminado in lista_contactos:
                lista_contactos.pop(eliminado)
                lista_nombres.remove(eliminado)
                print("contacto eliminado con exito.")
            else:
                print("usuario no encontrado.")
                input("""
presione enter para volver.
""")

        elif interfaz == "4":
            if not lista_nombres:
                input("""
aún no haz agendado a nadie. Presione enter para volver.
""")
            else:
                print(f"""En tu lista de contactos se encuentran las siguientes personas: 
                    """)
                for nombre in lista_nombres:
                    print(f"-{nombre}")
                input("""
presione enter para volver.
""")

        elif interfaz == "5":
            entrada = input("Contacto a modificar: ").capitalize()
        
            if entrada in lista_contactos:
                try:
                    modificacion = input("""
1 - Modificar nombre.
2 - Modificar número.
3 - Modificar mail.
Ingrese una opción: """)

                    if modificacion == "1":
                        nombre_mod = input("Ingrese nuevo nombre: ").capitalize()
                        
                        # Copiar la información y eliminar el contacto viejo
                        lista_contactos[nombre_mod] = lista_contactos.pop(entrada)
                        
                        # Actualizar la lista de nombres
                        lista_nombres.append(nombre_mod)
                        lista_nombres.remove(entrada)

                        input("\nContacto modificado con éxito. Presione enter para volver.")

                    elif modificacion == "2":
                        numero_mod = input("Ingrese nuevo número: ")
                        try:
                            int(numero_mod)  # Verificar si es número válido
                            lista_contactos[entrada][0] = numero_mod  # Solo modificar el número

                            input("\nNúmero modificado con éxito. Presione enter para volver.")
                            
                        except ValueError:
                            input("\nNúmero inválido. Presione enter para volver.")

                    elif modificacion == "3":
                        mail_mod = input("Ingrese nuevo mail: ")
                        lista_contactos[entrada][1] = mail_mod  # Solo modificar el mail

                        input("\nMail modificado con éxito. Presione enter para volver.")

                    else:
                        input("\nOpción inválida. Presione enter para volver.")

                except:
                    input("\nEntrada inválida. Presione enter para volver.")

            else:
                input(f"\nEl contacto '{entrada}' no se encuentra en su lista de contactos. Presione enter para volver.")

        elif interfaz == "6":
            break
    
    except:
        print("entrada invalida.")
        input("vuelva a intentar.")