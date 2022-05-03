class Car:
    def __init__(self, model: str, color: str, cost: str):
        self.model = model
        self.color = color
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.model}: {self.color}, {self.cost} млн рублей"

    def change(self, ch_color, ch_cost):
        self.color = ch_color
        self.cost = ch_cost


'''
car1 = Car('Bmw', "Белый", "1")
print(car1)

car1.change(ch_color='Black', ch_cost='2')
print(car1)

car1.change(ch_color='Blue', ch_cost='0.78')
print(car1)
'''


class Truck:
    def __init__(self, carry_capacity=0, cargo=None):
        if cargo is None:
            cargo = {}
        self.c_p = carry_capacity
        self.crg = cargo

    def add_cargo(self, ch_cargo, mass: int):
        self.crg.update({ch_cargo: mass})
        self.c_p = self.c_p - mass

    def rm_cargo(self, ch_cargo):
        try:
            self.c_p = self.c_p + self.crg.get(ch_cargo)
            self.crg.pop(ch_cargo)
        except:
            print(f'cargo: "{ch_cargo.upper()}" - not found')

    def __str__(self) -> str:
        if self.crg == {}:
            return f"Вместимость {self.c_p}, Груз: EMPTY"
        else:
            return f"Вместимость {self.c_p}, Груз: {self.crg}"


truck1 = Truck(carry_capacity=60)
print(truck1)
truck1.add_cargo('apple', 15)
print(truck1)
truck1.add_cargo('icecream', 18)
print(truck1)
truck1.add_cargo('potatoes', 20)
print(truck1)
truck1.rm_cargo('potato')
print(truck1)
truck1.rm_cargo('potatoes')
print(truck1)
truck1.rm_cargo('icecream')
print(truck1)
truck1.rm_cargo('apple')
print(truck1)
