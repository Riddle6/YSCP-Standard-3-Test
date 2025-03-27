# Global dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():

    contact_name = input("\nEnter the contact's name: ").strip().capitalize()

    contacts[contact_name] = {} # Nested Dictionary created
        
    contact_number = input("Enter the contact's phone number: ").strip()
    contact_email = input("Enter the contact's email address: ").strip()

    contacts[contact_name][contact_number] = contact_email
    # Value of the nested dictionary is set to the contact email.

    print(f"\nContact for {contact_name} added successfully.\n")
    
    
# Function to view all contacts
def display_contacts():
    
    if contacts == {}:
        print("\nNo Contacts Available.\n")
    else:
        print("\n--- All Contacts ---")
        for key, value in contacts.items():
            print(f"{contacts}: Phone - {contacts[key]} \n")
        

# Function to search for a contact by name
def search_contact():
    
    search_contacts = input("Enter the name of the contact to search for: ").strip()

    if search_contacts in contacts:
        print(f"Contacts found: {contacts} ") # W.I.P
    
    else:
        print(f"Contacts for {search_contacts} not found.")

# Function to remove a contact
def remove_contact():

    remove_contacts = input("Enter the name of the contact to remove: ").strip() 

    if remove_contacts in contacts:
        contacts.pop(remove_contacts)
        print(f"Contact for {remove_contacts} removed successfully!\n")

    else:
        print(f"\nContacts for {remove_contacts} not found.\n")


# Function to update a contact's information
def update_contact():

    update_contacts = input("Enter the name of the contact to update: ").strip()

    if update_contacts in contacts:
        new_number = input("Enter the new phone number: ").strip()

        new_email = input("Enter the new email address: ").strip()
        # W.I.P
        

    else:
        print(f"Contacts for {update_contacts} not found.")

# Main function to run the menu-driven system
def main():

    while True:
        option = display_menu()
        

        if option == 1:
            add_contact()
            
        elif option == 2:
            display_contacts()

        elif option == 3:
            search_contact()

        elif option == 4:
            remove_contact()

        elif option == 5:
            update_contact()

        elif option == 6:
            print("\nThank you for using Contact Manager!")
            print("Goodbye!")
            break

        else:
            print("Unforeseen Error!")


def display_menu():
    print("--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Seach for a Contact")
    print("4. Remove a Contact")
    print("5. Update a Contact")
    print("6. Quit\n")

    while True:
        try:
            option = int(input("Choose an option (1-6): "))

            if option >= 1 and option <= 6:
                return option
            else:
                print("\nOption out of range! Please try again.\n")
            
        except ValueError:
            print("\nError! That is not a number! Please try again.\n")

if __name__ == "__main__":
    main()
