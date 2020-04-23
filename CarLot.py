import csv
from pathlib import Path
from FileHandler import FileHandler


class CarLot:
    def __init__(self):
        self.file_handler = FileHandler()

    def get_fleet_size(self):
        number_of_vehicles = 0
        try:
            cars = self.file_handler.load_from_csv('Vehicle.csv')
            for row in cars:
                number_of_vehicles += 1
            return number_of_vehicles

        except Exception as e:
            print("Error: " + str(e))
            return False


car_lot = CarLot()
print(car_lot.get_fleet_size())

# print(car_lot.update_salary_by_name('User.csv',1500, 111111))
