import csv
import os
from collections import OrderedDict


class User:
    def user_auth(name):
        with open('D:\\Anna\\Bootcamp exercises\\python\\Python-mini-project\\User.csv') as users_file:
            users_file_reader = csv.reader(users_file)
            for row in users_file_reader:
                if row[1] == name:
                    print(row)
                    return (row[6])
                else:
                    return False





print(User.user_auth("Anna"))
