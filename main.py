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
    "M":  0x07
}

var = {
    "A":  0x00,
    "B":  0x01,
    "C":  0x02,
    "D":  0x03,
    "E":  0x04,
    "F":  0x05,
    "G":  0x06,
    "M":  0x07
}

var2 = {
    "A":  0x07,
    "B":  0x0A,
    "C":  0x12,
    "D":  0x1A,
    "E":  0x22,
    "F":  0x2A,
    "G":  0x32,
}

movMem = {
    "A":  0x06,
    "B":  0x09,
    "C":  0x11,
    "D":  0x19,
    "E":  0x21,
    "F":  0x29,
    "G":  0x31,
}

print("8-Bit CPU assembler")
print("Enter file name to assemble (Make sure it is a .txt file and in the same directory): ", end="")

filename = input()

file = open(filename, "r")
content = file.readlines()
file.close()

output = open(filename.replace(".txt", ".asm"), "w")


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
            output.write(str(movRegVars[line[1]]))
            if line[1] == "B" or line[1] == "D" or line[1] == "F" or line[1] == "M":
                output.write(format(var[line[2]]+8, "01X"))
                output.write("\n")
            else:
                output.write(str(var[line[2]]))
                output.write("\n")
        else:
            output.write(format((var[line[1]] << 3) + 3, "02X"))
            output.write("\n")
            output.write(format(int(line[2]), "02X"))
            output.write("\n")
    #ADD Command
    elif line[0] == "ADD":
        if not line[1].isdigit():
            output.write("8")
            output.write(str(var[line[1]]))
            output.write("\n")
        else:
            output.write("80")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #ADC command
    elif line[0] == "ADC":
        if not line[1].isdigit():
            output.write("8")
            output.write(format(var[line[1]]+8, "01X"))
            output.write("\n")
        else:
            output.write("88")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #SUB command
    elif line[0] == "SUB":
        if not line[1].isdigit():
            output.write("9")
            output.write(str(var[line[1]]))
            output.write("\n")
        else:
            output.write("90")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #SBC command
    elif line[0] == "SBC":
        if not line[1].isdigit():
            output.write("9")
            output.write(format(var[line[1]]+8, "01X"))
            output.write("\n")
        else:
            output.write("98")
            output.write("\n")
            output.write(str(int(line[1])))
            output.write("\n")
    #AND command
    elif line[0] == "AND":
        if not line[1].isdigit():
            output.write("A")
            output.write(str(var[line[1]]))
            output.write("\n")
        else:
            output.write("A0")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #OR command
    elif line[0] == "OR":
        if not line[1].isdigit():
            output.write("A")
            output.write(format(var[line[1]]+8, "01X"))
            output.write("\n")
        else:
            output.write("A8")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #CMPE command 
    elif line[0] == "CMPE":
        if not line[1].isdigit():
            output.write("B")
            output.write(str(var[line[1]]))
            output.write("\n")
        else:
            output.write("B0")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #XCHG command
    elif line[0] == "XCHG":
        if not line[1].isdigit():
            output.write("B")
            output.write(format(var[line[1]]+8, "01X"))
            output.write("\n")
        else:
            output.write("B8")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #CMPD command
    elif line[0] == "CMPD":
        if not line[1].isdigit():
            output.write("C")
            output.write(format(var[line[1]]+8, "01X"))
            output.write("\n")
        else:
            output.write("C8")
            output.write("\n")
            output.write(format(int(line[1]), "02X"))
            output.write("\n")
    #MOVF command
    elif line[0] == "MOVF":
        output.write(format(var2[line[1]], "02X"))
        output.write("\n")
    #SHR command
    elif line[0] == "SHR":
        output.write("08")
        output.write("\n")
    #SHL command
    elif line[0] == "SHL":
        output.write("10")
        output.write("\n")
    #NOP command
    elif line[0] == "NOP":
        output.write("0")
        output.write("\n")
    #CPL command
    elif line[0] == "CPL":
        output.write("01")
        output.write("\n")
    #JMP command
    elif line[0] == "JMP":
        if len(line) > 1:
            output.write("32")
            output.write("\n")
            output.write(format(line[1], "02X"))
            output.write("\n")
            output.write(format(line[2], "02X"))
            output.write("\n")
        else:
            output.write("04")
            output.write("\n")
    #CALL command
    elif line[0] == "CALL":
        output.write("05")
        output.write("\n")
    #RET command
    elif line[0] == "RET":
        output.write("0C")
        output.write("\n")

print("Assembled!")

output.close()




        




    