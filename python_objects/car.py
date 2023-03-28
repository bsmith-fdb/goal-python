from vehicle import Vehicle


class Car(Vehicle):
    default_tire = '16in'

    def __init__(self, engine, tires=None, distance_traveled=0, unit='feet', **kwargs):
        super().__init__(distance_traveled=distance_traveled, unit=unit, **kwargs)
        if not tires:
            tires = [self.default_tire, self.default_tire, self.default_tire, self.default_tire]
        self.tires = tires
        self.engine = engine

    def drive(self, distance):
        self.distance_traveled += distance

    def description(self):
        initial = super().description()
        return f"{initial} on {self.tires} tires"
