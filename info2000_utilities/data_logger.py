# this logs data
import os
import time
class Logger:
    def __init__(self, file_destination):
        self.path = file_destination
        # if file doesn't exist, let's create it
        if not os.path.exists(self.path):
            # create the file
            with open(self.path, 'w') as f:
                ...
                pass
    def logrow(self, data):
        t = time.localtime()
        t = time.strftime('%HH:%MM:%SS', t)
        with open(self.path, 'a') as f:
            f.write(t+','+data)
            f.write('\n')