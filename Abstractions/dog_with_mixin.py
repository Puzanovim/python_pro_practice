
class RollOverMixin:
    def roll_over(self):
        print("Done roll over!")


class SpeakMixin:
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f"{name} speak: \"Hello!\"")


class Dog(SpeakMixin, RollOverMixin):
    pass


dog = Dog()
dog.roll_over()
dog.speak()
