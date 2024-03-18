class Avengers:
    Shield = []
    name = "Nub"
    power = 1

    def __init__(self, name, power):
        self.__name = name
        self.__power = power
        print(self.__name, "become Avenger! with a power equal:", self.__power)
        Avengers.Shield.append(self)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def print_person(self):
        print(f"Имя: {self.__name}\tСила: {self.__power}")

    @staticmethod
    def generalFee():
        print()
        for avenger in Avengers.Shield:
            print("| The ", avenger.__name)
        print("\nAll Avengers become in general fee!")


AV1 = Avengers("Klark", 99)
AV2 = Avengers("Halk", 101)
AV3 = Avengers("IronMan", 77)
AV4 = Avengers("Arrow", 0)

Avengers.generalFee()

AV2.name = "Havchik"
AV2.print_person()
print(AV2.name)
