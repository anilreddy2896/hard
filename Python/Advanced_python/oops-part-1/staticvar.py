# static variable is same to all the obbjects
class Team():
    # 1:
    game="cricket"
    def __init__(self,name,team,country):
        self.name=name
        self.team=team
        self.country=country
        Test.
    def about(self):
        print("player_name:",self.name)
        print("team",self.team)
        print("country:",self.country)
        #accessing with in the class so we need to use self
        print("game",self.game)
t=Team("virat","rcb","india")
t.about()
##accessing using object reference
print(t.game)
##accessing using class
print(Team.game)
print(t.__dict__)