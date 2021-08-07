class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print('Inhale, Exhale! ')


class Fish(Animal):

    def breathe(self):
        super().breathe()
        print('Breathe under water')


nemo = Fish()

nemo.breathe()
