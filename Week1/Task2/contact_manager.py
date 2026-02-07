import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=2)
    print("Contacts saved!")

def add_contact():
    contacts = load_contacts()
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    save_contacts(contacts)

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

while True:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Exit")
    choice = input("Choose option: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break