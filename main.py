from cpu import CPU
from memory import Memory

cpu = CPU()
memory = Memory()

# Initialize registers
cpu.registers["A"] = 5
cpu.registers["B"] = 10

print("Altair Emulator: CPU and Memory Initialized!")

# Write ADD instruction to memory and execute it
memory.write(0x1000, 0x80)  # 0x80 = ADD B to A
instruction = memory.read(0x1000)
cpu.execute_instruction(instruction)

#print ("Altair Emulator: Ready to Run")
#print ("Hello World")