class Stadion:
    def __init__(self, model="", year=0, country="", city ="", Capacity = 0.0):
        self.__model = model
        self.__year = year
        self.__country = country
        self.__city = city
        self.__Capacity = Capacity

    @property
    def price(self):
        return self.__Capacity

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__Capacity = value
        else:
            print("Ошибка: Вместимость не может быть отрицательной!")


    def __str__(self):
        return (f"Стадион {self.__model} ({self.__year} г.)\n"
                f":Страна {self.__country}\n"
                f"Вместимость: {self.__Capacity}\n"
                f"Город: {self.__city}")

stadion = Stadion("Барселона",1945, "Испания" , "Берлин", 50000 )

print(stadion)