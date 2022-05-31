class Transport:
    def __init__(self, name):
        self.name = name


class Auto(Transport):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed


class Truck(Auto):
    def __init__(self, weight, name, speed):
        self.weight = weight
        super().__init__(name, speed)


class Car(Auto):
    def __init__(self, name, speed, model):
        super().__init__(name, speed)
        self.model = model


class Bus(Transport):
    def __init__(self, name, number_of_passengers):
        super().__init__(name)
        self.number_of_passengers = number_of_passengers


class Trolleybus(Transport):
    def __init__(self, name, last_stop):
        super().__init__(name)
        self.last_stop = last_stop


class Tram(Transport):
    def __init__(self, name, initial_stop):
        super().__init__(name)
        self.initial_stop = initial_stop

