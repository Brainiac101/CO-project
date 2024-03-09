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

def add(l, dict):
    return "0000000" + dict(l[3]) + dict[l[2]] + "000" + dict[l[1]] + "0110011";

def sub(l, dict):
    return "0100000" + dict[l[3]] + dict[l[2]] + "000" + dict[l[1]] + "0110011";
    
def sll(l, dict):
    return "0000000" + dict[l[3]] + dict[l[2]] + "001" + dict[l[1]] + "0110011";

def slt(l, dict):
    return "0000000" + dict[l[3]] + dict[l[2]] + "010" + dict[l[1]] + "0110011";

def sltu(l, dict):
    return "0000000" + dict[l[3]] + dict[l[2]] + "011" + dict[l[1]] + "0110011";

def xor(l, dict):
    return "0000000" + dict[l[3]] + dict[l[2]] + "100" + dict[l[1]] + "0110011";

def srl(l, dict):
    return "0000000" + dict[l[3]] + dict[l[2]] + "101" + dict[l[1]] + "0110011";

def ory(l, dict):
    return "0000000" + dict[l[3]] + dict[l[2]] + "110" + dict[l[1]] + "0110011";

def andy(l, dict):
    return "0000000" + dict[l[3]] + dict[l[2]] + "111" + dict[l[1]] + "0110011";

dict={"zero" : "00000", "ra":"00001", "sp": "00010", "gp":"00011", "tp":"00100", "t0":"00101", "t1":"00110", "t2":"00111", "s0":"01000", "fp":"01000", "s1":"01001", "a0":"01010", "a1":"01011", "a2": "01100", "a3":"01101", "a4":"01110", "a5":"01111", "a6":"10000", "a7":"10001", "s2":"10010", "s3":"10011", "s4": "10100", "s5":"10101", "s6":"10110", "s7":"10111", "s8":"11000", "s9":"11001", "s10": "11010", "s11":"11011", "t3": "11100", "t4":"11101", "t5":"11110", "t6":"11111"}
fin = open("sample.txt", "r")
fout=open("output.txt", "w")
for line in fin:
    l=split(line)
    if l[0]=="add":
        fout.write(add(l, dict))
    elif l[0]=="sub":
        fout.write(sub(l, dict))
    elif l[0]=="sll":
        fout.write(sll(l, dict))
    elif l[0]=="slt":
        fout.write(slt(l, dict))
    elif l[0]=="sltu":
        fout.write(sltu(l, dict))
    elif l[0]=="xor":
        fout.write(xor(l, dict))
    elif l[0]=="srl":
        fout.write(srl(l, dict))
    elif l[0]=="or":
        fout.write(ory(l, dict))
    elif l[0]=="and":
        fout.write(andy(l, dict))
    fout.write("\n")
fin.close()
fout.close()
