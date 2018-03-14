import os

class BaseCar:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)



class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(self):
            self.car_type = str(self.__class__.__name__).lower()


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(self):
            self.car_type = str(self.__class__.__name__).lower()


class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(self):
            self.car_type = str(self.__class__.__name__).lower()


def get_car_list(csv_filename):
    car_list = []
    return car_list