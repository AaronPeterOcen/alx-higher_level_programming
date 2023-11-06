##0756968024


class Animal:
    def __init__(self, birthType="?", appearence="?", blood="?"):
        self.birthType = birthType
        self.appearence = appearence
        self.blood = blood

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearence(self):
        return self.__appearence

    @appearence.setter
    def appearence(self, appearence):
        self.__appearence = appearence

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, blood):
        self.__blood = blood

    def __str__(self):
        return "A {} is {} it is {} it is {}".format(
            type(self).__name__, self.birthType, self.appearence, self.blood
        )


class Mammal(Animal):
    def __init__(
        self,
        birthType="born Alive",
        appearence="hair / fur",
        blood="wb",
        nurseYoung=True,
    ):
        Animal.__init__(self, birthType, appearence, blood)

        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + " and it is {} they nurse " "their young".format(
            self.nurseYoung
        )


class Reptile(Animal):
    def __init__(
        self,
        birthType="born in an egg or born alive",
        appearance="dry scales",
        blood="cold blooded",
    ):
        # Call for the super class to initialize fields
        Animal.__init__(self, birthType, appearance, blood)

    # Operator overloading isn't necessary in Python because
    # Python allows you to enter unknown numbers of values
    # Always make sure self is the first attribute in your
    # class methods
    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i

        return sum
