import os.path

def main():
    file_name = "бумага.txt"

    while True:

        print("\nДоступные команды: create, add, view, exit")
        command = input("Введите команду: ")

        if command == "create":

            with open(file_name, "w", encoding="utf-8") as file:
                pass
            print(f"Файл '{file_name}' создан и очищен.")

        elif command == "add":

            note = input("Введите текст заметки: ")
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(note + "\n")
            print("Заметка добавлена.")

        elif command == "view":
            if not os.path.exists(file_name):
                print("Файл не найден")
                continue

            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()

                if not lines:
                    print("Файл пуст.")
                else:
                    for index, line in enumerate(lines, start=1):

                        print(f"{index}.")

        elif command == "exit":
            print("Выход")
            break

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()