class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_capacity=0.0, color="", price=0.0):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Ошибка: Цена не может быть отрицательной!")


    def __str__(self):
        return (f"Автомобиль: {self.__model} ({self.__year} г.)\n"
                f"Производитель: {self.__manufacturer}\n"
                f"Двигатель: {self.__engine_capacity}\n"
                f"Цвет: {self.__color}\n"
                f"Цена: {self.__price:} руб.")


car1 = Car("Tesla Model 3", 2023, "Tesla", 2.0, "White", 500)
print(car1)