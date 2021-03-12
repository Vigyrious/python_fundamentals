class Zoo:
    __animals = 0


    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.bird = []

    def add_animal(self,species,name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        else:
            self.bird.append(name)
        Zoo.__animals += 1


    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        else:
            result += f"Birds in {self.name}: {', '.join(self.bird)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    current = input().split(" ")
    zoo.add_animal(current[0],current[1])


show_me = input()
print(zoo.get_info(show_me))
