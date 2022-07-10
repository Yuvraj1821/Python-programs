from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def info(self):
        pass
        # print(" Function of Base class called")   #we can give definition to abstract method


class Derive1(Base):
    def info(self):
        print(" Function of first derived class is called ")


class Derive2(Base):
    def info(self):
        print(" Function of second derived class is called ")


# base = Base()     # We can not give physical form to abstract class / We cannot create object of abstract class
# base.info()

derive1 = Derive1()
derive1.info()

derive2 = Derive2()
derive2.info()
