#Завдання1

def total_salary(path):
    total_salary = 0
    count = 0

    try:
        with open(path_salary, "r") as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total_salary += float(salary)
                    count += 1
                except ValueError:
                    print('Incorrect string found')
                    continue
    except FileNotFoundError:
        print("File not found")
        return 0, 0

    if count == 0:
        print("No salary found")
    else:
        average = total_salary / count
        return average, total_salary

path_salary = "/Users/user/PycharmProjects/Homework/Salary.txt"

print(total_salary(path_salary))

#Завдання 2

def get_cats_info(path):
    cats_info = []
    with open(path_cats_info, "r") as file:
        for line in file:
            try:
                id, name, age = line.strip().split(',')

                cats_info.append ({
                    "id": id,
                    "name": name,
                    "age": age
                })
            except ValueError:
                print("Incorrect data found")
                continue
    return cats_info

path_cats_info = "/Users/user/PycharmProjects/Homework/CatsInfo.txt"
print(get_cats_info(path_cats_info))


#Завдання 4

def parse_input(user_input: str):
    cmd, *args = user_input.strip().lower().split()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Please enter name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Please enter name and phone number."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Please enter a username."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    print(
        "Commands:\n"
        "hello\n"
        "add [name] [phone]\n"
        "change [name] [phone]\n"
        "phone [name]\n"
        "all\n"
        "close / exit"
    )

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError:
                print("Please enter name and phone number.")

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


