def split(string):
    temp="";
    l=[];
    for i in string:
        if i == " " or i == "," or i == ":"  or i=="(":
            if temp=="":
                continue;

            l.append(temp);
            temp="";
            continue;

        else:
            temp+=i;
    if temp[-1]=="\n":
        temp=temp[:-1]
    l.append(temp);
    return l;

def add(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "000" + d[l[1]] + "0110011";

def sub(l,d):
    return "0100000" + d[l[3]] + d[l[2]] + "000" + d[l[1]] + "0110011";
    
def sll(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "001" + d[l[1]] + "0110011";

def slt(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "010" + d[l[1]] + "0110011";

def sltu(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "011" + d[l[1]] + "0110011";

def xor(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "100" + d[l[1]] + "0110011";

def srl(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "101" + d[l[1]] + "0110011";

def ory(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "110" + d[l[1]] + "0110011";

def andy(l,d):
    return "0000000" + d[l[3]] + d[l[2]] + "111" + d[l[1]] + "0110011";
d={"zero" : "00000", "ra":"00001", "sp": "00010", "gp":"00011", "tp":"00100", "t0":"00101", "t1":"00110", "t2":"00111", "s0":"01000", "fp":"01000", "s1":"01001", "a0":"01010", "a1":"01011", "a2": "01100", "a3":"01101", "a4":"01110", "a5":"01111", "a6":"10000", "a7":"10001", "s2":"10010", "s3":"10011", "s4": "10100", "s5":"10101", "s6":"10110", "s7":"10111", "s8":"11000", "s9":"11001", "s10": "11010", "s11":"11011", "t3": "11100", "t4":"11101", "t5":"11110", "t6":"11111"}
labels={}
fin = open("sample.txt", "r")
fout = open("output.txt", "w")
pc=0
a=fin.readlines()
for line in a:
    l=split(line);
    if len(l)>4:
        labels[l[0]]=pc*4;
    pc+=1;

pc=0
for line in a:
    l=split(line)
    if len(l)!=4:
        l=l[1::];
    d1={"add":add(l,d),"sub":sub(l,d),"sll":sll(l,d),"slt":slt(l,d),"sltu":sltu(l,d),"xor":xor(l,d),"srl":srl(l,d),"or":ory(l,d),"and":andy(l,d)}
    fout.write(d1[l[0])
    fout.write("\n")
    pc+=1;

fin.close()
fout.close()
