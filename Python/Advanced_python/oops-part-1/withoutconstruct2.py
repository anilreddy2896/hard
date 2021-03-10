class Movie():
    def vd(self, name,hero,director,rating):
        self.name=name
        self.hero=hero
        self.director=director
        self.rating=rating
    def info(self):
        print("moive name:",self.name)
        print("hero is:",self.hero)
        print("director is",self.director)
        print("rating is:",self.rating)
        print()

m=Movie()
m.vd("ls","nc","sk",200)
m.info()