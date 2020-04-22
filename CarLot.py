import csv
from pathlib import Path
from FileHandler import FileHandler


class CarLot:

    # def update_salary_by_name(self, file_name, employee_salary, id):
    #
    #     try:
    #         loaded_data = self.load_from_csv(file_name)
    #
    #
    #         for row in loaded_data:
    #             print(row)
    #             if row[6] == 'employee' and row[0] == id:
    #                 print(row)
    #         #         return row[6]
    #         # else:
    #         #     return False
    #     except Exception as e:
    #         print(e)


    def get_fleet_size(self):
        number_of_vehicles = 0
        try:
            cars = (FileHandler()).load_from_csv('Vehicle.csv')
            columns = cars.pop(0)
            print(columns)

            for row in cars:
                number_of_vehicles += 1
            return number_of_vehicles

        except Exception as e:
            print("Error: " + str(e))
            return False


car_lot = CarLot()
print(car_lot.get_fleet_size())

# print(car_lot.update_salary_by_name('User.csv',1500, 111111))
