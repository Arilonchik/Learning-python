import os
import csv

class CarBase:
    """The base class for all cars"""
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        """Get the ext of car photo file"""
        return os.path.splitext(self.photo_file_name)[1]


class Truck(CarBase):
    """Truck car"""
    def __init__(self, photo_file_name, brand, carrying, whl):
        super().__init__('Truck', photo_file_name, brand, carrying)
        try:
            self.body_width, self.body_height, self.body_length = map(int, whl.split('x'))
        except (ValueError, TypeError):
            self.body_width, self.body_height, self.body_length = (0, 0, 0)

    def get_body_volume(self):
        """Return body volume of the truck"""
        return self.body_height * self.body_length * self.body_width


class Car(CarBase):
    """Simple car"""
    def __init__(self, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__('Car', photo_file_name, brand, carrying)
        self.passenger_seat_count = passenger_seats_count


class SpecMachine(CarBase):
    """SpecMachine car"""
    def __init__(self, photo_file_name, brand, carrying, extra):
        super().__init__('SpecMachine', photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(path):
    cars = []
    with open(path) as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            ctype, brand, sc, pfn, whl, carr, extra = row
            if '' in [ctype, brand, pfn, carr]:
                continue
            if ctype == 'car':
                if sc == '':
                    continue
                cars.append(Car(pfn, brand, carr, sc))
            if ctype == 'truck':
                if whl == '':
                    continue
                cars.append(Truck(pfn, brand, carr, whl))
            if ctype == 'spec_machine':
                if extra == '':
                    continue
                cars.append(SpecMachine(pfn, brand, carr, extra))
            print(cars[-1].__dict__)

    return cars


print(get_car_list('data.csv'))
