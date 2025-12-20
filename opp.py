from OOP import TaskManager
from OOP import TaskManager

task_manager = TaskManager()
manager = TaskManager()

def main():

    while True:
        command = input("Введите (add/done/show/exit): ")

        if command == "add":
            title = input("Введите название задачи!")
            if title:
                manager.add_task(title)
                print("Задача добавлена!")
            else:
                print("Название не может быть пустым")

        elif command == "done":
            manager.show_tasks()
            if manager.tasks:
                try:
                    num = int(input("Номер задачи для отметки: "))
                    if 1 <= num <= len(manager.tasks):
                        manager.tasks[num - 1].mark_done()
                        print("Задача отмечена как выполненная.")
                    else:
                        print("Неверный номер.")
                except:
                    print("Введите номер.")

        elif command == "show":

            if manager.tasks:
                manager.show_tasks()

            else:
                print("Задач нету")

        elif command == "exit":
            manager.save_to_file()
            print("Данные сохарнены.Досвидания!")
            break
        else:
            print("Не известная команда")


if __name__ == "__main__":
    main()


