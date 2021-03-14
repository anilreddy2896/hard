## composition or HAS-A-RELATION    
class Engine:
    a=10
    
    def __init__(self):
        b=100
        print("Engine function")
    def test(self):
        print("successfully tried")
class car:
    def __init__(self):
        self.engine=Engine()
        self.m2()

    def m2(self):
        print(Engine.a)
        print(self.engine.test())
c=car()
        