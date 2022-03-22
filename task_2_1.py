documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people_name(numbers):
    for document in documents:
        if numbers == document["number"]:
            return document["name"]


def number_directories(numbers):
    for directory in directories:
        if numbers in directories.get(directory):
            return directory


def list_documents():
    for document in documents:
        print(list(document.values())[0], '"' + list(document.values())[1] + '"',
              '"' + list(document.values())[2] + '"')
    return True


def add_documents(type, number, name, number_direct):
    if number_direct in directories:
        directories[number_direct].append(number)
        documents.append({'type': type, 'number': number, 'name': name})
        return True
    else:
        return False


def delete(number):
    for document in documents:
        if number == document["number"]:
            documents.remove(document)
            for directory in directories:
                if number in directories.get(directory):
                    directories.get(directory).remove(number)
            return True
    return False


def move(number_doc, number_direct):
    for directory in directories:
        if number_doc in directories.get(directory):
            if number_direct in directories:
                if number_doc in directories.get(directory):
                    directories.get(directory).remove(number_doc)
                    directories[number_direct].append(number_doc)
                    return print(f'Документ {number_doc} успешно перемещен.'), True
            else:
                return print('Такой полки нет'), False
    return print('Такого документа нет'), False


def add_shelf(number_direct):
    if number_direct not in directories:
        directories[number_direct] = []
        return True
    else:
        return False


def help():
    return '''p – (people) – команда, которая выведет имя человека, которому принадлежит документ;
s – (shelf) – команда, выведет номер полки, на которой находится документ;
l– (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – (add) – команда, которая добавит новый документ в каталог и в перечень существующих полок;
d – (delete) – команда, которая удалит номер документа из каталога и из перечня полок;
m – (move) – команда, которая переместит документ с текущей полки на целевую существующую;
as – (add shelf) – команда, которая добавит номер полки в перечень;
q - выход из программы.\n'''


def secretary_program_start():
    while True:
        command = input('Введите команду(p, l, s, a, q, d, m, as, h(чтобы вывести справку)): ')
        if command == 'p':
            numbers = input('Введите номер документа: ')
            print(f'Владелец документа: {people_name(numbers)}')
        elif command == 's':
            numbers = input('Введите номер документа: ')
            print(f"Номер полки: {number_directories(numbers)}")
        elif command == 'l':
            list_documents()
        elif command == 'a':
            type = input('Введите тип документа: ')
            number = input('Введите номер документа: ')
            name = input('Введите имя владельца: ')
            number_direct = input('Введите номер полки: ')
            add_doc = add_documents(type, number, name, number_direct)
            if add_doc == False:
                print('Такой полки не существует!')
        elif command == 'q':
            break
        elif command == 'd':
            number = input('Введите номер документа для удаления: ')
            del_ = delete(number)
            if del_ == False:
                print('Такого документа нет')
        elif command == 'm':
            number_doc = input('Введите номер документа: ')
            number_direct = input('Введите номер полки: ')
            move(number_doc, number_direct)
        elif command == 'as':
            number_direct = input('Введите номер новой полки: ')
            add_shelf_ = add_shelf(number_direct)
            if add_shelf_ == False:
                print('Такая полка уже существует')
        elif command == 'h':
            print(help())


if __name__ == '__main__':
    secretary_program_start()

