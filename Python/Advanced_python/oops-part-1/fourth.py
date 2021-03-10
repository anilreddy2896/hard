## creating objects using the list
class Movie():
    def __init__(self, name,hero,director,rating):
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
movies = [Movie("lovestory","nagchaithanya","shekhar",98), 
          Movie("bhahubali","prabhas","ssrajamouli",100),
          Movie("happydays","unkown","kamula",200)]
for i in movies:
    i.info()