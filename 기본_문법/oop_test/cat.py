from oop_test.animal import Animal

class Cat(Animal):
    sound = "야옹~~"

    def __init__(self, name, age, is_indoor=True):
        super().__init__(name, age)
        self.is_indoor = is_indoor

    def make_sound(self):
        print(f"{self.name}: {Cat.sound}")