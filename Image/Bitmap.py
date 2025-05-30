
class handler():
    ff = ".bmp"

    def __init__(self, name):
        filename = name + self.ff
        header = 'BM'
        infoheader = ""

    def write(self):
        f = open(self.filename, "w")