import os
import csv

class BaseCar:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.car_type = str(self.__class__.__name__).lower()
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except:
            raise BaseException('parsed carrying badly')
    
    def get_photo_file_ext(self):
        file_ext = os.path.splitext(self.photo_file_name)
        return file_ext[1] if file_ext else ''


class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except:
            raise BaseException('parsed passenger_seats_count')


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl = None):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_width, self.body_height, self.body_length = body_whl.split('x')
            self.body_width, self.body_height, self.body_length = float(self.body_width), float(self.body_height), float(self.body_length)
        except:
            self.body_width, self.body_height, self.body_length = (0,0,0)
    
    def get_body_volume(self):
        return self.body_width*self.body_height*self.body_length


class Spec_Machine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        car_params_keys = next(reader)  # dict keys
        for row in reader:
            try:
                car_params = {car_params_keys[idx]:param for idx, param in enumerate(row) if param!=''}
                car_type = car_params.pop('car_type')
                # print(car_type, car_params)
                if car_params:
                    if car_type == 'car':
                        car = Car(**car_params)
                    elif car_type == 'truck':
                        car = Truck(**car_params)
                    elif car_type == 'spec_machine':
                        car = Spec_Machine(**car_params)
                    else:
                        continue
                    car_list.append(car)
                # print(car.__dict__)
            except (KeyError, TypeError):
                continue
    return(car_list)

# got_cars = get_car_list('C:/Users/YSTARUKHIN/Desktop/edu/py_learning/playgrnd/cars.csv')
# for car in got_cars: print(car.__dict__)