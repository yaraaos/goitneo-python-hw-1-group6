def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_username_phone(args, contacts):
    username, phone = args
    contacts[username] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    phone, username = args
    contacts[phone] = username
    return "Phone changed."

def phone_username(args, contacts):
    username = args[0]
    if username in contacts:
        return contacts[username]
    else:
        return "Contact not found"

def all_contacts(contacts):
    for username, phone in contacts.items():
        print(f"Username: {username}, Phone: {phone}")
    


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_username_phone(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "all":
            all_contacts(contacts)
        elif command == "call":
            print(phone_username(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()