# # ## 🟦 1-TOPSHIRIQ (DO‘KON / MAHSULOTLAR)
#
# from abc import ABC, abstractmethod
#
# class Product(ABC):
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#     def __init__(self, name, price, categories,in_stock):
#         self.__name = name
#         self.__price = price
#         self.categories = categories
#         self.in_stock = in_stock
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, value):
#         self.__name = value
#     @name.deleter
#     def name(self):
#         del self.__name
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, value):
#         self.__price = value
#     @price.deleter
#     def price(self):
#         del self.__price
#
#
# class ElectronicProduct(Product):
#     def get_info(self):
#         return f"{self.name} - {self.price}"
#
#     def __init__(self, name, price, categories,in_stock,warranty_years):
#         super().__init__(name, price, categories,in_stock)
#         self.__warranty_years = warranty_years
#     @property
#     def warranty_years(self):
#         return self.__warranty_years
#     @warranty_years.setter
#     def warranty_years(self, value):
#         self.__warranty_years = value
#     @warranty_years.deleter
#     def warranty_years(self):
#         del self.__warranty_years
#
# ep1 = ElectronicProduct("Laptop", 1200, [], True, 2)
# ep2 = ElectronicProduct("Phone", 800, [], True, 1)
#
# ep1.categories.append("Electronics")
# ep2.categories.append("Mobile")
#
# print(getattr(ep1, "name"))
#
# setattr(ep1, "price", 1100)
#
# print(hasattr(ep1, "warranty_years"))
#
# delattr(ep1, "warranty_years")
# print(ep1.__dict__)
#
#
# # ep2 uchun
# print(getattr(ep2, "name"))
#
# setattr(ep2, "price", 900)
#
# print(hasattr(ep2, "in_stock"))
#
# delattr(ep2, "warranty_years")
# print(ep2.__dict__)

# ----------------------------------------------------------------------------

# 2. Team nomli ABSTRACT class yarating.

from abc import ABC, abstractmethod


class Team(ABC):
    def __init__(self, team_name, coach, players, country):
        self.__team_name = team_name
        self.__coach = coach
        self.players = players
        self.country = country

    @abstractmethod
    def get_info(self):
        pass

    @property
    def team_name(self):
        return self.__team_name

    @team_name.setter
    def team_name(self, value):
        self.__team_name = value

    @team_name.deleter
    def team_name(self):
        del self.__team_name

    @property
    def coach(self):
        return self.__coach

    @coach.setter
    def coach(self, value):
        self.__coach = value

    @coach.deleter
    def coach(self):
        del self.__coach

class FootballTeam(Team):
    def __init__(self, team_name, coach, players, country, stadium):
        super().__init__(team_name, coach, players, country)
        self.__stadium = stadium

    def get_info(self):
        return f"{self.team_name} ({self.coach})"

    @property
    def stadium(self):
        return self.__stadium

    @stadium.setter
    def stadium(self, value):
        self.__stadium = value

    @stadium.deleter
    def stadium(self):
        del self.__stadium


    @staticmethod
    def is_full_team(players_list):
        return len(players_list) >= 11

f1 = FootballTeam(
    "Liverpool",
    "Klopp",
    [ "Alisson", "Alexander-Arnold", "Van Dijk", "Konate", "Robertson",
        "Wirtz", "Szoboszlaidominik", "Alemacallister", "Salah", "Mané", "Stevengerrard"],
    "Angliya",
    "Anfield"
)

f2 = FootballTeam(
    "Mancity",
    "Pep",
    [ "Donnarumma", "Khusanov", "Doku", "Erling", "Foden",
        "niko", "Cherki", "savinho", "Marmuos", "nathanake", "Laporte"],
    "Angliya",
    "Etihad"
)

# ##f1
print(getattr(f1, "team_name"))
setattr(f1, "players", f1.players + ["Alex_isak"])
print(getattr(f1, "players"))
print(FootballTeam.is_full_team(f1.players))
print(hasattr(f1, "stadium"))
delattr(f1, "_FootballTeam__stadium")
print(f1.__dict__)


# ##f2
print(getattr(f2, "team_name"))
setattr(f2, "players", f2.players + ["Silva"])
print(getattr(f2, "players"))
print(FootballTeam.is_full_team(f2.players))
print(f2.__dict__)

