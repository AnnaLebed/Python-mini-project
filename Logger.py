from datetime import datetime
import logging
import os


class Logger:

    def add_to_log(msg):
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime("%d-%b-%Y %H:%M:%S-")
        location = "D:\\Anna\\Bootcamp exercises\\python\\Python-mini-project"
        try:
            f = open(os.path.join(location + 'log.txt'))
            f.write(timestamp_str + " " +msg + "\n")
        except Exception as e:
            print("error logging {}, error is {}".format(msg, e.args[0]))



first = 'second test string'
Logger.add_to_log(first)


