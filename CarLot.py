import csv

class CarLot:


    def update_salary_by_name(employee_salary,name):








    def get_fleet_size():
        number_of_vehicles = 0
        try:
            with open('D:\\Anna\\Bootcamp exercises\\python\\Python-mini-project\\Vehicle.csv') as file:
                csv_reader_object = csv.reader(file)
                if csv.Sniffer().has_header:
                    next(csv_reader_object)
                for row in csv_reader_object:
                    number_of_vehicles += 1
            return number_of_vehicles

        except FileNotFoundError as e:
            print(e)
            print("There is no file with such name!")



print(CarLot.get_fleet_size())