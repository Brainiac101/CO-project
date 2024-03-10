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
def decimal_to_twos_complement(decimal_num):
    if decimal_num < 0:
        abs_decimal = abs(decimal_num)
        complement = 2**32 - abs_decimal
    else:
        complement = decimal_num

    twos = bin(complement)[2:]
    
    if len(twos) < 32:
        twos = '0' * (32 - len(twos)) + twos

    return twos
def beq(l):
    global d;
    return decimal_to_twos_complement(int(l[3]))[19]+" "+decimal_to_twos_complement(int(l[3]))[21:27]+" " + d[l[2]] + d[l[1]] + "000" + " "+decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20]+" "+ "1100011";

def bne(l):
    global d;
    return  decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27]+ d[l[2]] + d[l[1]] + "001" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def blt(l):
    global d;
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "100" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def bge(l):
    global d;
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "101" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def bltu(l):
    global d;
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "110" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def bgeu(l):
    global d;
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "111" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";
d={"zero" : "00000", "ra":"00001", "sp": "00010", "gp":"00011", "tp":"00100", "t0":"00101", "t1":"00110", "t2":"00111", "s0":"01000", "fp":"01000", "s1":"01001", "a0":"01010", "a1":"01011", "a2": "01100", "a3":"01101", "a4":"01110", "a5":"01111", "a6":"10000", "a7":"10001", "s2":"10010", "s3":"10011", "s4": "10100", "s5":"10101", "s6":"10110", "s7":"10111", "s8":"11000", "s9":"11001", "s10": "11010", "s11":"11011", "t3": "11100", "t4":"11101", "t5":"11110", "t6":"11111"}
labels={}
fin = open("sample.txt", "r")
fout = open("output.txt", "w")
pc=0
a=fin.readlines()
for line in fin:
    l=split(line);
    if len(l)>4:
        labels[l[0]]=pc*4;
    pc+=1;

pc=0
for line in a:
    l=split(line)
    if len(l)!=4:
        labels[l[0]]=pc;
        l=l[1::];
    d1={"beq":beq(l),"bne":bne(l),"blt":blt(l),"bge":bge(l),"bltu":bltu(l),"bgeu":bgeu(l)} 
    fout.write(d1[l[0]])
    fout.write("\n")
    pc+=1;

fin.close()
fout.close()
