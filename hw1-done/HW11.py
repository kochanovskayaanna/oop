import os
import csv


def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        cars = csv.reader(csv_fd, delimiter=';')
        next(cars)
        for row in cars:
            if len(row) != 7:
                continue
            car_type = row[0]
            brand = row[1]
            passenger_seats_count = row[2]
            photo_file_name = row[3]
            body_whl = row[4]
            carrying = row[5]
            extra = row[6]
            try:
                if car_type == "car":
                    car = Car(brand, photo_file_name, carrying, passenger_seats_count)
                elif car_type == "truck":
                    car = Truck(brand, photo_file_name, carrying, body_whl)
                elif car_type == "spec_machine":
                    car = SpecMachine(brand, photo_file_name, carrying, extra)
                else:
                    continue
            except AssertionError as ae:
                print(ae)
                continue
            car_list.append(car)
    return car_list


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        assert brand != '' and photo_file_name != '' and carrying != '', "Empty fields"
        self.photo_file_name = photo_file_name
        assert self.get_photo_file_ext() in [".jpg", ".jpeg", ".png", ".gif"], "Invalid extension for photo file"
        self.brand = brand
        assert isfloat(carrying), "Invalid value for carrying"
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        assert passenger_seats_count.isdigit(), "Invalid value for passenger seats count (or empty)"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        self.body_width, self.body_height, self.body_length = self.parse_whl(body_whl)

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    @staticmethod
    def parse_whl(body_whl):
        whl_list = body_whl.split('x')
        if len(whl_list) != 3:
            return 0, 0, 0
        else:
            try:
                return float(whl_list[0]), float(whl_list[1]), float(whl_list[2])
            except ValueError:
                return 0, 0, 0


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


if __name__ == "__main__":
    pass
    # car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
    # print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
    # truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
    # print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')
    # spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
    # print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
    # cars = get_car_list('coursera_week3_cars.csv')
    # print(len(cars))
    # print(cars[0].passenger_seats_count)
    # print(cars[1].get_body_volume())

