import B-type as b
import I-type as i
import J-type as j
import R-type as r
import S-type as s
import U-type as u

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
d={"zero" : "00000", "ra":"00001", "sp": "00010", "gp":"00011", "tp":"00100", "t0":"00101", "t1":"00110", "t2":"00111", "s0":"01000", "fp":"01000", "s1":"01001", "a0":"01010", "a1":"01011", "a2": "01100", "a3":"01101", "a4":"01110", "a5":"01111", "a6":"10000", "a7":"10001", "s2":"10010", "s3":"10011", "s4": "10100", "s5":"10101", "s6":"10110", "s7":"10111", "s8":"11000", "s9":"11001", "s10": "11010", "s11":"11011", "t3": "11100", "t4":"11101", "t5":"11110", "t6":"11111"}
rtype=["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]
btype=["beq", "bne", "blt", "bge", "bltu", "bgu"] 
itype=["lw","addi","sltiu","jalr"]
jtype=["jal"]
utype=["auipc","lui"]
stype=["sw"]
labels={}
fin = open("sample.txt", "r")
fout = open("output.txt", "w")
pc=0
a=fin.readlines()
for line in a:
    l=split(line);
    if len(l)>4:
        labels[l[0]]=pc*4;
    if l[1] in ["lui", "jal","auipc"] and len(l)!=3:
        labels[l[0]]=pc*4;
    pc+=1;
pc=0
for line in a:
    l=split(line)
    if len(l)>4:
        l=l[1::];
    if l[1] in ["lui", "jal","auipc"] and len(l)!=3:
        l=l[1::]
    d1={}
    str=""
    if l[0] in rtype:
        d1={"add":r.add(l, d), "sub":r.sub(l, d),"sll":r.sll(l, d),"slt":r.slt(l, d),"sltu":r.sltu(l, d),"xor":r.xor(l, d),"srl":r.srl(l, d),"or":r.ory(l, d),"and":r.andy(l, d)};
        str=d1[l[0]]
    elif l[0] in btype:
        d1={"beq":b.beq(l, d,labels,pc), "bne":b.bne(l, d,labels,pc), "blt":b.blt(l, d,labels,pc), "bge":b.bge(l, d,labels,pc), "bltu":b.bltu(l, d,labels,pc), "bgeu":b.bgeu(l, d,labels,pc)}
        str=d1[l[0]]
    elif l[0] in itype:
        d1={"lw":i.lw(l,d),"addi":i.addi(l,d),"sltiu":i.sltiu(l,d),"jalr":i.jalr(l,d)}
        str=d1[l[0]]
    elif l[0] in stype:
        d1={"sw":s.sw(l,d)}
        str=d1[l[0]]
    elif l[0] in jtype:
        d1={"jal":j.jal(l,d)}
        str=d1[l[0]]
    elif l[0] in utype:
        d1={"auipc":u.auipc(l,d),"lui":u.lui(l,d)}
        str=d1[l[0]]
    else:
        fout.write("error "+str(pc))
    fout.write(str)
    fout.write("\n")
    pc+=1;
    

