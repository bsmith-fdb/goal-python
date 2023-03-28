class Vehicle:
    """
    Vehicle is a type that describes a machine that helps us travel
    """
    class_variable = "foo"

    # default_tire = 'tire'
    def __init__(self, distance_traveled=0, unit='miles', **kwargs):
        """
        Customizes the initialization of the object
        """
        self.distance_traveled = distance_traveled
        self.unit = unit
        # self.engine = engine
        # self.tires = tires

    # decorators
    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)

    @staticmethod
    def funk():
        print("hello from funk")

    def description(self):
        return f"DistanceTraveled={self.distance_traveled} Unit={self.unit}"


if __name__ == "__main__":
    civic = Vehicle("1.8L 4-cyl", "14-in all weather radial")
    civic.description()
    civic.foo = "a dynamic attribute"
    print(dir(civic))
    bike = Vehicle.bicycle(['700mm', '700mm'])
    bike.description()
    Vehicle.funk()
    bike.funk()
