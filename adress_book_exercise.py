contact_list = {}  # Dictionary to store contacts with name as the key and a list [phone, email] as the value
name_list = []  # List to keep track of contact names

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
        if interface == "1":  # Adding a contact
            name = input("Name of the new contact: ").capitalize()
            phone = input("Phone number: ")
            email = input("Email of the new contact: ")
            try:
                int(phone)  # Checking if the phone number is a valid integer
                contact_list[name] = [phone, email]  # Storing the contact in the dictionary
                name_list.append(name)  # Adding the name to the name list
                input("""
Contact saved successfully. Press enter to return.
""")

            except ValueError:
                print("Invalid phone number.")
                input("""
Press enter to return.
""")

        elif interface == "2":  # Searching for a contact
            entry = input("Name of the contact: ").capitalize()
            contact = contact_list.get(entry)  # Getting the contact details from the dictionary
            if contact is None:  # If contact doesn't exist
                print("Contact not found.")
                input("""
Press enter to return.
""")

            else:  # Displaying the contact details if found
                print(f"""
            Name: {entry}
            Number: {contact[0]}
            Email: {contact[1]}
            
""")
                input("""
Press enter to return.
""")

        elif interface == "3":  # Deleting a contact
            deleted = input("Contact to delete: ").capitalize()
            if deleted in contact_list:  # Checking if the contact exists
                contact_list.pop(deleted)  # Removing the contact from the dictionary
                name_list.remove(deleted)  # Removing the name from the name list
                print("Contact successfully deleted.")
            else:
                print("User not found.")
                input("""
Press enter to return.
""")

        elif interface == "4":  # Viewing all contacts
            if not name_list:  # If there are no contacts in the list
                input("""
You haven't saved any contacts yet. Press enter to return.
""")
            else:
                print(f"""The following people are in your contact list: 
                    """)
                for name in name_list:
                    print(f"- {name}")  # Displaying all saved contact names
                input("""
Press enter to return.
""")

        elif interface == "5":  # Modifying a contact
            entry = input("Contact to modify: ").capitalize()
        
            if entry in contact_list:  # Checking if the contact exists
                try:
                    modification = input("""
1 - Modify name.
2 - Modify number.
3 - Modify email.
Enter an option: """)

                    if modification == "1":  # Modifying the contact's name
                        new_name = input("Enter new name: ").capitalize()

                        if new_name not in name_list:  # Checking if the new name already exists
                            contact_list[new_name] = contact_list.pop(entry)  # Renaming the contact
                            name_list.append(new_name)  # Adding the new name to the name list
                            name_list.remove(entry)  # Removing the old name from the list

                            input("\nContact successfully modified. Press enter to return.")
                        else:
                            input("\nA contact with that name already exists. Press enter to return.")

                    elif modification == "2":  # Modifying the phone number
                        new_number = input("Enter new number: ")
                        try:
                            int(new_number)  # Checking if the new number is valid
                            contact_list[entry][0] = new_number  # Updating the phone number

                            input("\nNumber successfully modified. Press enter to return.")
                            
                        except ValueError:
                            input("\nInvalid number. Press enter to return.")

                    elif modification == "3":  # Modifying the email
                        new_email = input("Enter new email: ")
                        contact_list[entry][1] = new_email  # Updating the email

                        input("\nEmail successfully modified. Press enter to return.")

                    else:
                        input("\nInvalid option. Press enter to return.")

                except:
                    input("\nInvalid input. Press enter to return.")

            else:
                input(f"\nThe contact '{entry}' is not in your contact list. Press enter to return.")

        elif interface == "6":  # Closing the program
            break
    
    except:
        print("Invalid input.")  # Error handling for invalid options
        input("Please try again.")

