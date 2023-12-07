import os
class DataFile():

    def __init__(self, filename):

        if os.path.exists(filename):

            with open(filename, mode="r") as f:

                self.lines = [line.rstrip() for line in f]

        else:
            print("File does not exists")
            exit(1)
