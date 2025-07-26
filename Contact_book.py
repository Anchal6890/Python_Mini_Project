#Contact Book
contact = []

def show_menu():
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Name:")
    phone = input("Enter Phone Number:")
    email = input("Enter Email:")
    address = input("Enter Address:")
    contact.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
        })
    print("Contact added successfully!")

def view_contact():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nAll Contacts:")
        for i,contact in enumerate(contacts,start=1):
            print(f"\nContacts{i}:")
            print(f"Name:{contact['name']}")
            print(f"Phone:{contact['phone']}")
            print(f"Email:{contact['email']}")
            print(f"Address:{contact['address']}")

def search_contact():
    keyword = input("Enter the name to search:")
    for contact in contacts:
        if keyword.lower() == contact['name'].lower():
            print("\nContact Found:")
            print(f"Name:{contact['name']}")
            print(f"Phone:{contact['phone']}")
            print(f"Email:{contact['email']}")
            print(f"Address:{contact['address']}")
            return
        print("Contact not found.")

def update_contact():
    keyword = input("Enter the name of the contact to update.")
    for contact in contacts:
        if keyword.lower() == contact['name'].lower():
            print("Enter new details(leave blank to keep old value):")
            name = input(f"New name[{contact['name']}]:")or contact['name']
            phone = input(f"New phone[{contact['phone']}]:")or contact['phone']
            email = input(f"New email[{contact['email']}]:")or contact['email']
            address = input(f"New address[{address['address']}]:")or contact['address']     
            contact.update({"name":name,"phone":phone,"email":email,"address":address})
            print("Contact updated successfully!")
            return
            print("Contact not found.")

def delete_contact():
    keyword = input("Enter the name of the contact to delete:")
    for i,contact in enumerate(contacts):
        if keyword.lower()==contact['name'].lower():
            del contacts[i]
            print("Contact deleted successfully!")
            return
        print("Contact not found.")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice(1-6:"))
            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contact()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                update_contact()
            elif choice == 5:
                delete_contact()
            elif choice == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid choice.Please choose between 1to6.")
       except ValueError:
                    print("Invalid input.Please enter a number.")

main()
