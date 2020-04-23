import csv
import os
from pathlib import Path
from FileHandler import FileHandler


class User:
    def __init__(self):
        self.file_handler = FileHandler()

    def user_auth(self, id, password):

        try:
            users = self.file_handler.load_from_csv('User.csv')

            users.pop(0)

            for row in users:
                if int(row[0]) == int(id) and str(row[3]) == str(password):
                    return str(row[6])
                else:
                    return False

        except Exception as e:
            print(e)

    def update_salary_by_name(self, employee_salary, id):
        try:
            users = self.file_handler.load_from_csv('User.csv')

            columns = users.pop(0)

            for num, row in enumerate(users, start=0):
                if int(row[0]) == int(id):
                        # and str(row[3]) == "employee":
                    print(num, row)
                    print(row[7])
                    users.pop(num)
                    # users.insert(row[7], employee_salary)
                    break

            users.insert(0, columns)
            writer = csv.writer(open(self.file_handler.directory('User.csv'), 'w', newline=''))

            writer.writerows(users)

            return True
        except Exception as e:
            print("Error: " + str(e))
            return False


user1 = User()
# print(user1.user_auth("111111", "111111"))
print(user1.update_salary_by_name("100000", "333333"))
