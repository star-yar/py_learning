import os

class FileReader:
    def __init__(self, filename):
        self.filename = filename        
    
    def read(self):
        if not os.path.isfile(self.filename):
            return ""
        with open(self.filename) as f:
            return f.read()

reader = FileReader("example.txt")
print(reader.read())