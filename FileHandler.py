import csv
import os
import pathlib


class FileHandler:
    file_path = ''

    def __init__(self):
        self.file_path
        self.readen_data = []

    def directory(self, file_name):
        self.file_path = pathlib.Path(__file__).parent.absolute().joinpath(file_name)

    def load_from_csv(self, file_name):
        self.directory(file_name)
        try:
            self.readen_data = []

            with open(self.file_path) as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                for row in reader:
                    self.readen_data.append(row)
                # print(self.readen_data)

                # storing it in class just in case

        except FileNotFoundError as e:
            print(e)
            print("There is no file with such name!")

        return self.readen_data

    def write_to_file(self, data):
        try:

            print(self.readen_data[0])
            columns = self.readen_data.pop(0)
            if len(data) != len(self.readen_data[0]):
                raise Exception("Incorrect data structure")

            for row in self.readen_data:
                if int(row[0]) == int(data[0]):
                    raise Exception("Duplicated id found")

            with open(self.file_path, 'a') as fd:
                stringified_row = ", ".join(str(x) for x in data) + "\n"
                fd.write(stringified_row)

        except Exception as e:
            print(e)

    def append_to_csv(self, file_name, data):
        self.load_from_csv(file_name)
        self.write_to_file(data)

    def remove_from_csv(self, file_name, id):

        try:
            loaded_data = self.load_from_csv(file_name)
            columns = loaded_data.pop(0)

            for num, row in enumerate(loaded_data, start=0):
                if int(row[0]) == int(id):
                    loaded_data.pop(num)
                    break

            loaded_data.insert(0, columns)

            writer = csv.writer(open(self.file_path, 'w', newline=''))
            writer.writerows(loaded_data)
            return True

        except Exception as e:
            print("Error: " + str(e))
            return False

    # def update_csv(self, file_name, id, data):
    #     try:
    #        self.load_from_csv(file_name)
    #
    #
    #         columns =  self.readen_data.pop(0)
    #
    #
    #         for index, row in enumerate( self.readen_data, start=0):
    #             if int(row[0]) == int(id):
    #
    #                 self.readen_data.pop(index)
    #
    #
    #                 self.readen_data.insert(index, data)
    #                 break
    #
    #         # returning columns names back to the content (at the first place)
    #         self.readen_data.insert(0, columns)
    #
    #         # storing content back to the file
    #
    #         заменить
    #         на
    #         write
    #         to
    #         file:
    #
    #         self.write_to_file(data)
    #
    #         writer = csv.writer(open(self.get_file_path(file_name), 'w', newline=''))
    #
    #         writer.writerows(content)
    #
    #         return True
    #     except Exception as e:
    #         print("Error: " + str(e))
    #         return False

# fh = FileHandler()
# # fh.load_from_csv('User.csv')
#
#
# print(fh.append_to_csv('User.csv', [1001000, 'Daniel', 'Leffiz', '101010', 'manager', 20000, 'employee']))

# print(fh.remove_from_csv('user.csv', 888888))
#
#
#
