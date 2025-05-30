
class handler():
    ff = ".bmp"

    def __init__(self, name):
        self.filename = name + self.ff
        self.header = 'BM'
        self.infoheader = ""


    def write(self, path=None):

        if path == None:
            f = open(self.filename, "w")
        else:
            f = open(path + self.filename, "w")