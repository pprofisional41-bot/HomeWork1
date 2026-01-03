class Book:
    def __init__(self, model="", year=0, publisher="", author="", price=0.0):
        self.__model = model
        self.__year = year
        self.__publisher = publisher
        self.__author = author
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
        return (f"Книга: {self.__model} ({self.__year} г.)\n"
                f"Издатель: {self.__publisher}\n"
                f"Автор: {self.__author}\n"
                f"Цена: {self.__price:} руб.")


book_1 = Book("Мёртвые души", 1842, "Эксмо", "И.В.Гоголь",350000)
print(book_1)
