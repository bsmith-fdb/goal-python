from vehicle import Vehicle
from boat import Boat
from car import Car


class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires='6x33in', distance_traveled=0, unit='miles', **kwargs):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit, **kwargs)
        self.boat_type = 'motor'

    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"


if __name__ == "__main__":
    av = AmphibiousVehicle('12-cyl')
    print(av.description())
    print(AmphibiousVehicle.__mro__)  # method resolution order
    av.travel(100, 200)
    print(av.description())
    print(AmphibiousVehicle.__bases__)  # show classes inherited (<class 'car.Car'>, <class 'boat.Boat'>)
    print(Car.__subclasses__())  # show classes inheriting [<class '__main__.AmphibiousVehicle'>]
    print(hasattr(Boat, 'boat_type'))  # False
    boat = Boat()
    print(hasattr(boat, 'boat_type'))  # True
    print(hasattr(Car, 'default_tire'))  # True
    print(issubclass(Boat, Vehicle))  # True
    print(issubclass(Boat, AmphibiousVehicle))  # False
    print(issubclass(AmphibiousVehicle, Vehicle))  # True
    water_car = AmphibiousVehicle('8.0L 12-cyl')
    print(isinstance(water_car, Vehicle))  # True
    print(isinstance(water_car, Boat))  # True
    print(water_car.__dict__)  # {'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'tires': '6x33in', 'engine': '8.0L 12-cyl'}
    print(water_car.__str__())  # <AmphibiousVehicle {'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'tires': '6x33in', 'engine': '8.0L 12-cyl'}>
    print(str(water_car))  # <AmphibiousVehicle {'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'tires': '6x33in', 'engine': '8.0L 12-cyl'}>

