class animal:
    def __init__(self, name, is_alive, colour):
        self.name = name
        self.is_alive = is_alive
        self.colour = colour
    
class dog(animal):
    pass

class cat(animal):
    pass

d1 = dog("Rex", True, "Brown")
c1 = cat("Whiskers", True, "Black")
print(d1.name)
print(c1)