from vehicle import Vehicle


class Bicycle(Vehicle):
    default_tire = '26in'

    def __init__(self, tires=None, distance_traveled=0, unit='feet'):
        super().__init__(distance_traveled, unit)
        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tires = tires

    def description(self):
        initial = super().description()
        return f"{initial} on {self.tires} tires"


if __name__ == "__main__":
    bike = Bicycle(tires='700mm', distance_traveled=100)
    print(bike.description())
