import base
from utils import commands

print("Консольная программа специально для job.alif.tj")

print("""
Действии/Команды:
add:    Добавить в список
edit:   Изменить запись в списке
delete: Удалить из списка
result: Вычесть общую сумму
""")

while True:
    print("Вводите имя файла и действие (через пробел):", end=' ')
    filename, command = input().split()

    filename = filename.lower()
    command = command.lower()

    if command == "add":
        if not filename in base.files:
            base.files[filename] = {}

        commands().add(filename)

    elif command == "edit":
        if not filename in base.files:
            print(f"{filename} пустой !!!")
        else:
            commands().edit(filename)

    elif command == "delete":
        if not filename in base.files:
            print(f"{filename} пустой !!!")
        else:
            commands().delete(filename)

    elif command == "result":
        commands().result(filename)

    else:
        print("Такой команды не существует или вы неправильно вводили команду")