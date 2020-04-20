import csv
import os

class User:

    def user_auth(id,password):
        # location = "D:\\Anna\\Bootcamp exercises\\python\\Python-mini-project"
        try:
            # with open(os.path.join(location + 'User.csv') as users_file:
            with open('D:\\Anna\\Bootcamp exercises\\python\\Python-mini-project\\User.csv') as users_file:
                users_file_reader = csv.reader(users_file)

                for row in users_file_reader:
                    if row[0] == id and row[3] == password:
                        return row[6]
                else:
                    return False
        except Exception as e:
            print(e)


user1 = User
print(user1.user_auth("111111", "111111"))

