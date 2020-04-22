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


user1 = User()
print(user1.user_auth("111111", "111111"))

