from datetime import datetime
import logging


class Logger:

    def add_to_log(msg):
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime("%d-%b-%Y %H:%M:%S-")
        f = open("D:\\Anna\\Bootcamp exercises\\python\\Python-mini-project\\log.txt", "a")
        f.write(timestamp_str + " " +msg + "\n")



first = 'first test string'
Logger.add_to_log(first)



