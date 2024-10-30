class Parfum:
    
    discount = 10
    category = "Luxury"


    def __init__(self, volume=0, price=0.0, manufacturer="", order=0):
        self.__volume = volume
        self.__price = price
        self.__manufacturer = manufacturer
        self.__order = order


    def __del__(self):
        print(f"Об'єкт '{self.__manufacturer}' видалено.")


    def getVolume(self):
        return self.__volume

    def setVolume(self, volume):
        if volume > 0:
            self.__volume = volume
        else:
            print("Об'єм має бути більше 0.")

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Ціна не може бути від'ємною.")

    def getManufacturer(self):
        return self.__manufacturer

    def setManufacturer(self, manufacturer):
        if manufacturer:
            self.__manufacturer = manufacturer
        else:
            print("Виробник не може бути порожнім.")

    def getOrder(self):
        return self.__order

    def setOrder(self, order):
        if order:
            self.__order = order + self.__order
        else:
            print("Кількість не може бути від'ємною")


    def __str__(self):
        return f"Парфуми: {self.__manufacturer}, {self.__volume} мл, {self.__price} грн, {self.__order} шт"

    def __repr__(self):
        return f"Parfum(volume={self.__volume}, price={self.__price}, manufacturer='{self.__manufacturer}, order={self.__order}')"



def main():
    parfum1 = Parfum(50, 1200.0, "Chanel")
    parfum2 = Parfum(30, 800.0, "Dior")
    parfum3 = Parfum(100, 2500.0, "Gucci")

    print(parfum1)
    print(parfum2)
    print(parfum3)

    parfum1.setVolume(60)
    parfum1.setPrice(1100.0)

    print(f"Оновлені дані: {parfum1}")

    parfum_array = [parfum1, parfum2, parfum3]

    min_parfum = parfum_array[0]
    for parfum in parfum_array:
        if parfum.getOrder() < min_parfum.getOrder():
            min_parfum = parfum

    print(f"Парфум з найменшою кількістю продажів: {min_parfum}")

if __name__ == "__main__":
    main()
    