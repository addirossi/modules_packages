# import sqlalchemy

from test.main import var2

from data import documents, directories


class Secretary:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_person(self):
        number = input('Введите номер документа: ')
        for person in documents:
            if person['number'] == number:
                print(person['name'])
                break
        else:
            print('Человек с таким номером документа не зарегистрирован.')


    def get_shelf_number(self):
        number = input('Введите номер документа: ')
        for shelf, docs in directories.items():
            if number in docs:
                print(f'Документ с номером {number} находится на полке {shelf}')
                break
        else:
            print('Документ с таким номером не найден')


    def get_documents_list(self):
        for doc in documents:
            print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')


    def add_document(self):
        number = input("Введите номер документа: ")
        name = input("Введите имя и фамилию: ")
        doc_type = input("Введите тип документа: ")
        directory_number = input("Введите номер полки: ")
        if number and name and doc_type and directory_number:
            documents.append({'type': doc_type, 'number': number, 'name': name})
            if directory_number in directories:
                directories[directory_number].append(number)
            else:
                directories[directory_number] = [number]
        else:
            print('Введены не все данные')


def main():
    while True:
        secretary = Secretary('Maria', 'qwerty')
        command = input("Введите команду: ")
        if command == 'p':
            secretary.get_person()
        elif command == 's':
            secretary.get_shelf_number()
        elif command == 'l':
            secretary.get_documents_list()
        elif command == 'a':
            secretary.add_document()
        elif command == 'e':
            break

print(__name__)
if __name__ == '__main__':
    main()
