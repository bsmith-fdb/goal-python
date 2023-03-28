from vehicle import Vehicle


# **kwargs collect all additional parameters into a dict

class Boat(Vehicle):
    def __init__(self, boat_type='sail', distance_traveled=0, unit='feet', **kwargs):
        super().__init__(distance_traveled=distance_traveled, unit=unit, **kwargs)
        self.boat_type = boat_type

    def voyage(self, distance):
        self.distance_traveled += distance

    def description(self):
        initial = super().description()
        return f"{initial} using a {self.boat_type}"
