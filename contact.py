from printer import print_status, print_all_contact, print_contact

def add_contact(contacts: list[dict]):
    first_name = input("first name: ")
    last_name = input("last name: ")
    phone = input("phone: ")
    group = input("group (family, friend, work, other): ")

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })

    print_status('success')

def show_all_contact(contacts: list[dict]):

    if contacts:
        print_all_contact(contacts)
    else:
        print_status('error')


def search_contact(contacts):
    keyword = input("Ism yoki familiya kiriting: ").lower()
    found = False

    for c in contacts:
        if keyword in c["first_name"].lower() or keyword in c["last_name"].lower():
            print_contact(c)
            found = True

    if not found:
        print_status("error")


def delete_contact(contacts):
    phone = input("Telefon raqam kiriting (o‘chirish uchun): ")

    for c in contacts:
        if c["phone"] == phone:
            contacts.remove(c)
            print_status("success")
            return

    print_status("error")


def update_contact(contacts):
    phone = input("Qaysi kontaktni yangilaymiz (telefon raqam): ")

    for c in contacts:
        if c["phone"] == phone:
            c["first_name"] = input("Yangi ism: ")
            c["last_name"] = input("Yangi familiya: ")
            c["phone"] = input("Yangi telefon: ")
            c["group"] = input("Yangi guruh: ")
            print_status("success")
            return

    print_status("error")
