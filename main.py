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

    for i in range(len(line)):
        line[i] = line[i].strip()

    line[0] = line[0].upper()

    #MOV command
    if line[0] == "MOV":
        if not line[2].isdigit():
            print("0x", end="")
            print(movRegVars[line[1]], end="")
            print(var[line[2]], end="")
        else:
            print(hex((var[line[1]] << 3) + 3))
            print(hex(int(line[2])))
    #ADD Command
    elif line[0] == "ADD":
        if not line[1].isdigit():
            print("0x8", end="")
            print(hex(var[line[1]]))
        else:
            print("0x80")
            print(hex(int(line[1])))
    #ADC command
    elif line[0] == "ADC":
        if not line[1].isdigit():
            print("0x8", end="")
            print(var[line[1]]+8)
        else:
            print("0x88")
            print(hex(int(line[1])))
    #SUB command
    elif line[0] == "SUB":
        if not line[1].isdigit():
            print("0x9", end="")
            print(var[line[1]])
        else:
            print("0x90")
            print(hex(int(line[1])))
    #SBC command
    elif line[0] == "SBC":
        if not line[1].isdigit():
            print("0x9", end="")
            print(var[line[1]]+8)
        else:
            print("0x98")
            print(hex(int(line[1])))
    #CMPD command
    elif line[0] == "AND":
        if not line[1].isdigit():
            print("0xA", end="")
            print(var[line[1]])
        else:
            print("0xA0")
            print(hex(int(line[1])))
    #CMPD command
    elif line[0] == "OR":
        if not line[1].isdigit():
            print("0xA", end="")
            print(var[line[1]]+8)
        else:
            print("0xA0")
            print(hex(int(line[1])))
    #CMPD command
    elif line[0] == "CMPE":
        if not line[1].isdigit():
            print("0xB", end="")
            print(var[line[1]])
        else:
            print("0xB0")
            print(hex(int(line[1])))
    #CMPD command
    elif line[0] == "XCHG":
        if not line[1].isdigit():
            print("0xB", end="")
            print(var[line[1]]+8)
        else:
            print("0xB8")
            print(hex(int(line[1])))
    #CMPD command
    elif line[0] == "CMPD":
        if not line[1].isdigit():
            print("0xC", end="")
            print(var[line[1]]+8)
        else:
            print("0xC8")
            print(hex(int(line[1])))


    