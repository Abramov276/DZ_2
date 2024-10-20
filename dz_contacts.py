def parse_input(user_input):
    cmd, * args = user_input. split()
    cmd = cmd.strip().lower()
    return cmd, * args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments for 'add'. Use: add [name] [phone]"

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments for 'change'. Use: change [name] [new phone]"

    name, new_phone = args

    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Contact {name} not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid arguments for 'phone'. Use: phone [name]"

    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."


def show_all(contacts):

    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def main():
    contacts = {}
    print("Welcome to assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, * args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
