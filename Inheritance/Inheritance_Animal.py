class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class Mammal(Animal):

    def __init__(self, name, sound):
        Animal.__init__(self, name)

        self.sound = sound

    def feature(self):
        my_feature = Animal.display(self)

        return f"I am {my_feature}, And I do {self.sound}"

mam1 = Mammal("Dog","VauVau")
mam2 = Mammal("Cat", "MeoMeo")

print(mam1.feature())
print(mam2.feature())





# class Reptiles(Animal):
#     def feature(self):

