import gc
class Human:
    def __init__(self,name):
        self.name=name
        self.head=self.Head()
        self.brain=self.head.Brain()
        self.display()
    def display(self):
        print("hello ",self.name)
        self.head.talk()
        self.brain.think()


    class Head:
        def talk(self):
            print("talking")
        class Brain:
            def think(self):
                print("Thinking")
h=Human("anil")
#print(gc.isenabled())
print(gc.disable())
print(gc.enable())
print(gc.isenabled())