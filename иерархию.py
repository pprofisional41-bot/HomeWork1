class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.__position = position

    def get_position(self):
        return self.__position

    def display_info(self):
        return f"Имя: {self.get_name()}, Возраст: {self.get_age()}, Должность: {self.__position}"


class Manager(Employee):
    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self.__team = []

    def add_to_team(self, employee):
        if not isinstance(employee, Employee):
            raise ValueError("В команду можно добавить только объект типа Employee.")
        if employee == self:
            raise ValueError("Менеджер не может назначить самого себя в свою команду.")
        self.__team.append(employee)

    def display_team(self):
        print(f"\nКоманда менеджера {self.get_name()}:")
        if not self.__team:
            print("нет сотрудников.")
        else:
            for member in self.__team:
                print(f"  • {member.display_info()}")


