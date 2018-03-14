class Vault(list):
    def __init__(self, original_list=None):
        self.container = original_list or []
    
    def __getitem__(self, idx):
        return self.container[idx]
    
    def __setitem__(self, idx, value):
        self.container[idx] = value 

my_storage = Vault([1,2,3])
print(my_storage[1])
my_storage[2] = 1
print(my_storage[2])