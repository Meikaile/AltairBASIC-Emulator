class Memory:
    def __init__(self, size=65536):  # Default size: 64KB
        self.memory = [0] * size
    
    def read(self, address):
        return self.memory[address]
    
    def write(self, address, value):
        self.memory[address] = value

