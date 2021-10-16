class Road:

    def __init__(self, lengh, width):
        self.__lengt = lengh
        self.__width = width

    def get_weight(self, mass_asph, thick):
        return self.__lengt * self.__width * mass_asph * thick

road = Road(2000, 10)
print(road.get_weight(10, 15))