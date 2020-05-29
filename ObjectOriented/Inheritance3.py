class LivingBeing:

    def drink(self):
        print("Living beings need water/food to survive")


class NonLivingBeing:

    def eat(self):
        print("Non Living Things doesn't need any kind of resources to survive")


class Food(LivingBeing, NonLivingBeing):

    def foods(self):
        print("Human grows many kind of foods to eat")


F = Food()
F.foods()
F.drink()
F.eat()