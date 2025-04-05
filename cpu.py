class CPU:
    def __init__(self):
        # Initialize 8 general-purpose registers
        self.registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "H": 0, "L": 0}
        # Special registers
        self.program_counter = 0
        self.stack_pointer = 0

    def execute_instruction(self, instruction):
        # Print the instruction in hexadecimal format
        print(f"Executing: {hex(instruction)}")
        # Placeholder for CPU instruction handling


