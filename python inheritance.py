class Animal:
    def sleep(self):
        print("The animal is sleeping.")

    def height(self):
        pass  

    def eat(self):
        pass  


class Dog(Animal):
    def height(self):
        print("The dog is about 2 feet tall.")

    def eat(self):
        print("The dog is eating dog food.")


class Horse(Animal):
    def height(self):
        print("The horse is about 6 feet tall.")

    def eat(self):
        print("The horse is eating hay.")


class Snake(Animal):
    def height(self):
        print("The snake is about 1 foot long.")

    def eat(self):
        print("The snake is eating mice.")
    def sleep(self):
        print("The snake is eating mice.")



dog = Dog()
horse = Horse()
snake = Snake()


dog.sleep()
dog.height()
dog.eat()

horse.sleep()
horse.height()
horse.eat()

snake.sleep()
snake.height()
snake.eat()
