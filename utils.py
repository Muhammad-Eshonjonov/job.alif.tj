import base

class commands:
    def add(self, filename):
        print("Введите наименование и цену (через пробел):", end=' ')

        try:
            name, price = input().split()
        except:
            print("Вводите данные !!!")
            return

        if not price.isdigit():
            print("Цена должно быть числом !!!")
            return
        else:
            price = int(price)

        base.files[filename][name] = price

    def edit(self, filename):
        print("Введите наименование:", end=' ')
        try:
            name = input()
        except:
            print("Вводите данные !!!")
            return

        if not name in base.files[filename]:
            print(f"нету не какого '{name}' в '{filename}'")
        else:
            print(f"Введите новую цену {name}:", end=' ')
            try:
                price = input()
            except:
                print("Вводите данные !!!")
                return

            if not price.isdigit():
                print("Цена должно быть числом !!!")
                return
            else:
                price = int(price)

            base.files[filename][name] = price

    def delete(self, filename):
        print("Введите наименование:", end = ' ')
        try:
            name = input()
        except:
            print("Вводите данные !!!")
            return

        if name in base.files[filename]:
            del base.files[filename][name]
            print(f"{name} с {filename} успешно удален !!!")

        else:
            print(f"нету не какого '{name}' в '{filename}'")

    def result(self, filename):
        summa = 0
        for name in base.files[filename]:
            summa += base.files[filename][name]

        print("Сумма:", summa)