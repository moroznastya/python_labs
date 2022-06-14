class Resistor:
    def __init__(self, type: str, nominal: int, capacity: float, accuracy_in_percentage: float):
        self.type = type
        self.nominal = nominal
        self.capacity = capacity
        self.accuracy_in_percentage = accuracy_in_percentage

    def __str__(self):
        resistor_info = f'Resistor: type = {self.type},' \
                        f' nominal = {self.nominal}(Om), ' \
                        f'capacity = {self.capacity}(Bt),' \
                        f' accuracy = {self.accuracy_in_percentage} %'
        return resistor_info

