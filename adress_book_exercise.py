contact_list = {}
name_list = []

while True:

    print("""
Welcome to your address book.
1 - Add a contact.
2 - Search for a contact.
3 - Delete a contact.
4 - View contact list.
5 - Modify a contact.
6 - Close the program.
""")
    interface = input("Enter an option: ")
    try:
        if interface == "1": 
            name = input("Name of the new contact: ").capitalize()
            phone = input("Phone number: ")
            email = input("Email of the new contact: ")
            try:
                int(phone)
                contact_list[name] = [phone, email]
                name_list.append(name)
                input("""
Contact saved successfully. Press enter to return.
""")

            except ValueError:
                print("Invalid phone number.")
                input("""
Press enter to return.
""")

        elif interface == "2":
            entry = input("Name of the contact: ").capitalize()
            contact = contact_list.get(entry)
            if contact_list.get(entry) == None:
                print("Contact not found.")
                input("""
Press enter to return.
""")

            else: 
                print(f"""
            Name: {entry}
            Number: {contact[0]}
            Email: {contact[1]}
            
""")
                input("""
Press enter to return.
""")

        elif interface == "3":
            deleted = input("Contact to delete: ").capitalize()
            if deleted in contact_list:
                contact_list.pop(deleted)
                name_list.remove(deleted)
                print("Contact successfully deleted.")
            else:
                print("User not found.")
                input("""
Press enter to return.
""")

        elif interface == "4":
            if not name_list:
                input("""
You haven't saved any contacts yet. Press enter to return.
""")
            else:
                print(f"""The following people are in your contact list: 
                    """)
                for name in name_list:
                    print(f"- {name}")
                input("""
Press enter to return.
""")

        elif interface == "5":
            entry = input("Contact to modify: ").capitalize()
        
            if entry in contact_list:
                try:
                    modification = input("""
1 - Modify name.
2 - Modify number.
3 - Modify email.
Enter an option: """)

                    if modification == "1":
                        new_name = input("Enter new name: ").capitalize()

                        if new_name not in name_list:
                            contact_list[new_name] = contact_list.pop(entry)
                            
                            name_list.append(new_name)
                            name_list.remove(entry)

                            input("\nContact successfully modified. Press enter to return.")
                        else:
                            input("\nA contact with that name already exists. Press enter to return.")

                    elif modification == "2":
                        new_number = input("Enter new number: ")
                        try:
                            int(new_number)  
                            contact_list[entry][0] = new_number  

                            input("\nNumber successfully modified. Press enter to return.")
                            
                        except ValueError:
                            input("\nInvalid number. Press enter to return.")

                    elif modification == "3":
                        new_email = input("Enter new email: ")
                        contact_list[entry][1] = new_email  

                        input("\nEmail successfully modified. Press enter to return.")

                    else:
                        input("\nInvalid option. Press enter to return.")

                except:
                    input("\nInvalid input. Press enter to return.")

            else:
                input(f"\nThe contact '{entry}' is not in your contact list. Press enter to return.")

        elif interface == "6":
            break
    
    except:
        print("Invalid input.")
        input("Please try again.")
