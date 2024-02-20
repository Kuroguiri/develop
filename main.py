class Avengers:
    Shield = []
    name = "Nub"
    power = 1
    def __init__(self, name, power):
        self.name = name
        self.power = power
        print(self.name,"become Avenger! with a power equal:", self.power)
        Avengers.Shield.append(self)

    @staticmethod
    def generalFee():
        print()
        for avenger in Avengers.Shield:
            print("| The ",avenger.name)
        print("\nAll Avengers become in general fee!")


AV1 = Avengers("Klark", 99)
AV2 = Avengers("Halk", 101)
AV3 = Avengers("IronMan", 77)
AV4 = Avengers("Arrow", 0)

Avengers.generalFee()