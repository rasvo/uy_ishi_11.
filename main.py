# ## 🟦 1-TOPSHIRIQ (DO‘KON / MAHSULOTLAR)

from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def get_info(self):
        pass

    def __init__(self, name, price, categories,in_stock):
        self.__name = name
        self.__price = price
        self.categories = categories
        self.in_stock = in_stock

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @name.deleter
    def name(self):
        del self.__name
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = value
    @price.deleter
    def price(self):
        del self.__price


class ElectronicProduct(Product):
    def get_info(self):
        return f"{self.name} - {self.price}"

    def __init__(self, name, price, categories,in_stock,warranty_years):
        super().__init__(name, price, categories,in_stock)
        self.__warranty_years = warranty_years
    @property
    def warranty_years(self):
        return self.__warranty_years
    @warranty_years.setter
    def warranty_years(self, value):
        self.__warranty_years = value
    @warranty_years.deleter
    def warranty_years(self):
        del self.__warranty_years

ep1 = ElectronicProduct("Laptop", 1200, [], True, 2)
ep2 = ElectronicProduct("Phone", 800, [], True, 1)

ep1.categories.append("Electronics")
ep2.categories.append("Mobile")

print(getattr(ep1, "name"))

setattr(ep1, "price", 1100)

print(hasattr(ep1, "warranty_years"))

delattr(ep1, "warranty_years")
print(ep1.__dict__)


# ep2 uchun
print(getattr(ep2, "name"))

setattr(ep2, "price", 900)

print(hasattr(ep2, "in_stock"))

delattr(ep2, "warranty_years")
print(ep2.__dict__)






