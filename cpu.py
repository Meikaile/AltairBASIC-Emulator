class CPU:
    def __init__(self):
        # Initialize 8 general-purpose registers
        self.registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "H": 0, "L": 0}
        # Special registers
        self.program_counter = 0
        self.stack_pointer = 0

    def execute_instruction(self, instruction):
        # Keep the existing code for printing the instruction
        print(f"Executing: {hex(instruction)}")
        
        # Add new logic for handling the ADD operation
        if instruction == 0x80:  # Example: ADD B to A
            self.registers["A"] += self.registers["B"]
            self.registers["A"] &= 0xFF  # Ensure the result is 8-bit
            print(f"Performed ADD: A = {self.registers['A']}")
        else:
            print(f"Unknown instruction: {hex(instruction)}")



