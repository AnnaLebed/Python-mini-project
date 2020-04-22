import csv
import sys
import pathlib
import os


class FileHandler:
    __dbDir = ''

    # to create a full path from any file name
    def __init__(self):
        self.__dbDir = str(pathlib.Path(__file__).parent) + os.sep + "db"

    # to get the file path (without hardcoding)
    def get_file_path(self, file_name):
        return self.__dbDir + os.sep + file_name

    def load_from_csv(self, file_name):
        try:
            data = []
            with open(self.get_file_path(file_name)) as csv_file:
                reader = csv.reader(csv_file)

                for row in reader:
                    data.append(row)
        except FileNotFoundError as e:
            print(e)
            print("There is no file with such name!")
        return data

    def append_to_csv(self, file_name, new_data):
        try:
            loaded_data = self.load_from_csv(file_name)
            columns = loaded_data.pop(0)

            if len(columns) != len(new_data):
                raise Exception("Incorrect data structure. " + str(columns) + " expected")

            for row in loaded_data:
                if int(row[0]) == int(new_data[0]):
                    raise Exception("Duplicated id found")

            try:
                loaded_data.append(new_data)
                writer = csv.writer(open(self.get_file_path(file_name), 'a', newline=''))
                writer.writerow(new_data)

            except Exception as e:
                raise Exception("Error while trying to append to {} error is:{}".format(file_name, e))

            return True
        except Exception as e:
            print("Error: " + str(e))
            return False

    def remove_from_csv(self, file_name, id):
        try:
            loaded_data = self.load_from_csv(file_name)
            columns = loaded_data.pop(0)

            for num, row in enumerate(loaded_data, start=0):
                if int(row[0]) == int(id):
                    loaded_data.pop(num)
                    break

            loaded_data.insert(0, columns)
            writer = csv.writer(open(self.get_file_path(file_name), 'w', newline=''))
            writer.writerows(loaded_data)
            return True

        except Exception as e:
            print("Error: " + str(e))
            return False



fh = FileHandler()
# data = fh.load_from_csv('User.csv')
# print(data)
#
# print(fh.append_to_csv('User.csv', [281111, 'Daniel', 'Leffiz', '101010', 'manager', 20000, 'employee']))

print(fh.remove_from_csv('user.csv', 999999))
#
#
#

