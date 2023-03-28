from boat import Boat
from car import Car


class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires='6x33in', distance_traveled=0, unit='miles', **kwargs):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit, **kwargs)
        self.boat_type = 'motor'

    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)


if __name__ == "__main__":
    av = AmphibiousVehicle('12-cyl')
    print(av.description())
    print(AmphibiousVehicle.__mro__)  # constructor resolution order
    av.travel(100, 200)
    print(av.description())
