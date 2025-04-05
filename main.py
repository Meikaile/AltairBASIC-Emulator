from cpu import CPU
from memory import Memory

cpu = CPU()
memory = Memory()

print("Altair Emulator: CPU and Memory Initialized!")

# Example: Write to memory and execute a dummy instruction
memory.write(0x1000, 0x76)  # Example memory write
instruction = memory.read(0x1000)  # Read from memory
cpu.execute_instruction(instruction)


#print ("Altair Emulator: Ready to Run")
#print ("Hello World")