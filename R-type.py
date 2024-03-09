def split(string):
    temp="";
    l=[];
    for i in string:
        if i == " " or i == ",":
            l.append(temp);
            temp="";
            continue;
        else:
            temp+=i;
    if temp[-1]=="\n":
        temp=temp[:-1]
    l.append(temp);
    return l;

def add(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "000" + d[l[1]] + "0110011";

def sub(l):
    global d;
    return "0100000" + d[l[3]] + d[l[2]] + "000" + d[l[1]] + "0110011";
    
def sll(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "001" + d[l[1]] + "0110011";

def slt(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "010" + d[l[1]] + "0110011";

def sltu(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "011" + d[l[1]] + "0110011";

def xor(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "100" + d[l[1]] + "0110011";

def srl(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "101" + d[l[1]] + "0110011";

def ory(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "110" + d[l[1]] + "0110011";

def andy(l):
    global d;
    return "0000000" + d[l[3]] + d[l[2]] + "111" + d[l[1]] + "0110011";

def beq(l):
    global d;
    return " imm " + d[l[2]] + d[l[1]] + "000" + "imm part 2" + "1100011";

def bne(l):
    global d;
    return " imm " + d[l[2]] + d[l[1]] + "001" + "imm part 2" + "1100011";

def blt(l):
    global d;
    return " imm " + d[l[2]] + d[l[1]] + "100" + "imm part 2" + "1100011";

def bge(l):
    global d;
    return " imm " + d[l[2]] + d[l[1]] + "101" + "imm part 2" + "1100011";

def bltu(l):
    global d;
    return " imm " + d[l[2]] + d[l[1]] + "110" + "imm part 2" + "1100011";

def bgeu(l):
    global d;
    return " imm " + d[l[2]] + d[l[1]] + "111" + "imm part 2" + "1100011";

d={"zero" : "00000", "ra":"00001", "sp": "00010", "gp":"00011", "tp":"00100", "t0":"00101", "t1":"00110", "t2":"00111", "s0":"01000", "fp":"01000", "s1":"01001", "a0":"01010", "a1":"01011", "a2": "01100", "a3":"01101", "a4":"01110", "a5":"01111", "a6":"10000", "a7":"10001", "s2":"10010", "s3":"10011", "s4": "10100", "s5":"10101", "s6":"10110", "s7":"10111", "s8":"11000", "s9":"11001", "s10": "11010", "s11":"11011", "t3": "11100", "t4":"11101", "t5":"11110", "t6":"11111"}
fin = open("sample.txt", "r")
fout = open("output.txt", "w")
for line in fin:
    l=split(line)
    if l[0]=="add":
        fout.write(add(l))
    elif l[0]=="sub":
        fout.write(sub(l))
    elif l[0]=="sll":
        fout.write(sll(l))
    elif l[0]=="slt":
        fout.write(slt(l))
    elif l[0]=="sltu":
        fout.write(sltu(l))
    elif l[0]=="xor":
        fout.write(xor(l))
    elif l[0]=="srl":
        fout.write(srl(l))
    elif l[0]=="or":
        fout.write(ory(l))
    elif l[0]=="and":
        fout.write(andy(l))
    elif l[0]=="beq":
        fout.write(beq(l))
    elif l[0]=="bne":
        fout.write(bne(l))
    elif l[0]=="bge":
        fout.write(bge(l))
    elif l[0]=="bgeu":
        fout.write(bgeu(l))
    elif l[0]=="blt":
        fout.write(blt(l))
    elif l[0]=="bltu":
        fout.write(bltu(l))
    fout.write("\n")
fin.close()
fout.close()
