from abc import *
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass
class Child(Test):
    def m1(self):
        print("hello world thanks")

c=Child()
c.m1()