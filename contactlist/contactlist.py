class Contact:
    def __init__(self, name, phone, email):  #__init__ is like a constructor (auto create when object Contact are made)
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(f"Name : {self.name}")
        print(f"Phone Number : {self.phone}")
        print(f"Email : {self.email}")

contacts = [] 
# contacts = [
#     <Contact object: name="Muzan", phone="0123456789", email="muzan@email.com">,
#     <Contact object: name="Daniel", phone="0198765432", email="daniel@email.com">
# ]

def add_contact(new_contact):
    for contact in contacts:
        if contact.name.lower() == new_contact.name.lower():
            print("This name is already exist in the list of contact.")
            return
    contacts.append(new_contact)
    print(f"The new contact {new_contact} is added successfully")

def view_all_contact():
    if not contacts:
        print("The list is empty. Add first to see all contacts.")
        return
    print(f"{"Name":<25} {"Phone Number":<15} {"Email":<15} ")
    print("-"*60)
    for contact in contacts:
        print(f"{contact.name:<25} {contact.phone:<15} {contact.email:<15} ")

def search_contact(search_name):
    found = False
    for contact in contacts:
        if contact.name.lower() == search_name.lower():
            found = True
            contact.display()
            break
    if not found:
        print(f"This {search_name} are not added in the list before.")
            # print(f"Name: {contact.name}")
            # print(f"Phone Number: {contact.phone}")
            # print(f"Email: {contact.email}")


def delete_contact(name):
    if not contacts:
        print("The contact list is empty.")
        return
    found = False

    for i in range(len(contacts)):
        if contacts[i].name.lower() == name.lower():
            found = True
            contacts.pop(i)
            print(f"The {name} is deleted succesfully for the contact list.")
            break
    if not found:
        print(f"There is no {name} is the contact list")

while True:
    print("\n=== Contact Books ===")
    print("1. Add Contact")
    print("2. View All Contact ")
    print("3. Search Contact ")
    print("4. Delete Contact")
    print("5. Exit")

    try:
        choice = int(input("Choose an Option (1-5): "))
    except ValueError:
        print("Invalid Choice. Put only number in terminal.")
        continue

    if choice == 1:
        name = input("Enter the name: ")
        while True:
            try:
                phone = int(input("Enter the phone number: "))
                break
            except ValueError:
                print("Please enter only number for this part.")
                continue
        email = input("Enter the email: ")
        new_contact = Contact(name, phone, email)
        add_contact(new_contact)
    elif choice == 2:
        view_all_contact()
    elif choice == 3:
        name = input("Enter the name you want to SEARCH: ")
        search_contact(name)
    elif choice == 4:
        name = input("Enter the name you want to DELETE: ")
        delete_contact(name)
    elif choice == 5:
        print("Exiting.... GoodBye!")
        break
    else:
        print("Invalid input. You can only put 1-5.")