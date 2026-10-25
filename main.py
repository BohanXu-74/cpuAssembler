instructions = {
    "NOP":  0x01,
    "SUB":  0x02,
    "MUL":  0x03,
    "DIV":  0x04,
    "MOV":  0x05,
    "JMP":  0x06,
    "JEQ":  0x07,
    "JNE":  0x03,
    "JGT":  0x08,
    "JLT":  0x09,
    "PUSH": 0x00,
    "POP":  0x00
}

movRegVars = {
    "A":  0x04,
    "B":  0x04,
    "C":  0x05,
    "D":  0x05,
    "E":  0x06,
    "F":  0x06,
    "G":  0x07,
    "M":  0x07,
}

var = {
    "A":  0x00,
    "B":  0x01,
    "C":  0x02,
    "D":  0x03,
    "E":  0x04,
    "F":  0x05,
    "G":  0x06,
    "M":  0x07,
}

print("8-Bit CPU assembler")
print("Enter file name to assemble (Make sure it is a .txt file and in the same directory): ", end="")

filename = input()

file = open("code.txt", "r")
content = file.readlines()
file.close()

print("Assembling...")

for i in range(len(content)):
    line = content[i].replace(",", "")
    line = line.split(" ")
    command = line[0].upper()
    opcode1 = line[1].strip()
    opcode2 = line[2].strip()
    if command == "MOV":
        if not opcode2.isdigit():
            print(movRegVars[opcode1], end="")
            print(var[opcode2], end="")
        else:
            print(var[opcode1] << 3 + 3)
            print(int(opcode2))
    elif command == "ADD":
        if not opcode1.isdigit():
            print("8", end="")
            print(var[opcode1])
        else:
            print("80")
            print(opcode1)
    elif command == "ADC":
        if not opcode1.isdigit():
            print("8", end="")
            print(var[opcode1]+8)
        else:
            print("88")
            print(opcode1)
    elif command == "SUB":
        if not opcode1.isdigit():
            print("9", end="")
            print(var[opcode1])
        else:
            print("88")
            print(opcode1)
    elif command == "SBC":
        
