import csv

class FileHandler:

    def load_from_csv(file_name):
        try:
            with open(file_name) as csv_file:
                reader = csv.reader(csv_file, delimiter=',')

                count = 0
                for row in reader:
                    print(row)

                    if count > 5:
                        break

                        count +=1
        except FileNotFoundError as e:
            print(e)
            print("There is no file with such name!")


    def append_to_csv(file_name, data):
        with open(file_name, 'a') as fd:
            return fd.write(data)



FileHandler.load_from_csv('user.csv')
# append_to_csv('user.csv', Anna)