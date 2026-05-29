from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone):
        return phone.isdigit() and len(phone) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Додавання телефону
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Видалення телефону
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone number not found")

    # Пошук телефону
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    # Редагування телефону
    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)

        if phone_obj:
            if not Phone.validate_phone(new_phone):
                raise ValueError("New phone number must contain exactly 10 digits")
            phone_obj.value = new_phone
        else:
            raise ValueError("Old phone number not found")

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(UserDict):

    # Додавання запису
    def add_record(self, record):
        self.data[record.name.value] = record

    # Пошук запису
    def find(self, name):
        return self.data.get(name)

    # Видалення запису
    def delete(self, name):
        if name in self.data:
            del self.data[name]


# =========================
# ПРИКЛАД ВИКОРИСТАННЯ
# =========================

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")