import tempfile
import os

class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = ''
        if os.path.isfile(self.file_path):
            self.get_file_data() 

    def __str__(self):
        return self.file_path

    def write(self, text_to_write):
        with open(self.file_path, 'w') as f: f.write(text_to_write)
        self.file_data = self.get_file_data()
    
    def get_file_data(self):
        try:
            with open(self.file_path) as f: self.file_data = f.read()
        except:
            self.file_data = ''
        self.start = 0
        self.end = len(self.file_data.split('\n')) or 0
        self.current = 0
        return self.file_data

    def __add__(self, value_to_add):
        new_file = File(tempfile.gettempdir()+'/sum_file.txt')
        new_file.write(self.get_file_data()+value_to_add.get_file_data())
        return new_file
    
    def __iter__(self):
        if not self.file_data:
            self.file_data = self.get_file_data()
        return self

    def __next__(self):
        if self.end:
            if self.current >= self.end:
                raise StopIteration
            tmp_data = self.file_data.split('\n')[self.current]
            self.current+=1
            return tmp_data 

# obj = File('./file_class_testing.txt')
# obj.write('''this is tets file
# # body
# # end''')
# print(obj.file_data)
# myfile = File('123')
# myfile.write('abc')
# for line in myfile:
#     print(line)
# first = File('./tmp1.txt')
# first = File('./tmp1')
# print(first)
# print(first.file_data)
# second = File('./tmp2.txt')
# new_obj = first + second
# print(new_obj.get_file_data())
# # print(next(new_obj))
# # print(new_obj.get_file_data())
# # print('iter method:')
# for line in first:
#     print(line)

# # print(os.path.join('../tmp1.txt', '../tmp2.txt'))