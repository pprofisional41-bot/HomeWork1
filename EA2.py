from иерархию import Person
from иерархию import Employee
from иерархию import Manager


def main():
    employees = []
    while True:
        print("\nКоманды")
        print("1. Добавить сотрудника")
        print("2. Добавить менеджера")
        print("3. Назначить сотрудника в команду")
        print("4. Просмотреть всех сотрудников")
        print("5. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == '1' or choice == '2':
                name = input("Введите имя: ")
                age = int(input("Введите возраст: "))
                position = input("Введите должность: ")

                if choice == '1':
                    employees.append(Employee(name, age, position))
                else:
                    employees.append(Manager(name, age, position))
                print("Успешно добавлено.")


            elif choice == '3':
                if not employees:
                    print("Список сотрудников пуст.")
                    continue

                managers = [e for e in employees if isinstance(e, Manager)]
                if not managers:
                    print("В системе нет менеджеров.")
                    continue

                print("\nДоступные менеджеры:")
                for i, m in enumerate(managers):
                    print(f"{i}. {m.get_name()} ({m.get_position()})")

                m_idx = int(input("Выберите индекс менеджера: "))
                if not (0 <= m_idx < len(managers)):
                    raise IndexError("Менеджер с таким индексом не найден.")

                print("\nКого назначить в команду?")
                for i, e in enumerate(employees):
                    print(f"{i}. {e.get_name()} ({e.get_position()})")

                e_idx = int(input("Выберите индекс сотрудника: "))
                if not (0 <= e_idx < len(employees)):
                    raise IndexError("Сотрудник с таким индексом не найден.")

                managers[m_idx].add_to_team(employees[e_idx])
                print(f"Сотрудник успешно назначен к {managers[m_idx].get_name()}.")

            elif choice == '4':
                print("Список")
                for e in employees:
                    print(e.display_info())
                    if isinstance(e, Manager):
                        e.display_team()

            elif choice == '5':
                print("Завершение работы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")

        except ValueError as ve:
            print(f"Ошибка ввода: {ve}")
        except IndexError as ie:
            print(f"Ошибка поиска: {ie}")



if __name__ == "__main__":
    main()