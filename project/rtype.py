def add(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "000" + d[l[1]] + "0110011";

def sub(l, d):
    return "0100000" + d[l[3]] + d[l[2]] + "000" + d[l[1]] + "0110011";
    
def sll(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "001" + d[l[1]] + "0110011";

def slt(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "010" + d[l[1]] + "0110011";

def sltu(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "011" + d[l[1]] + "0110011";

def xor(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "100" + d[l[1]] + "0110011";

def srl(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "101" + d[l[1]] + "0110011";

def ory(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "110" + d[l[1]] + "0110011";

def andy(l, d):
    return "0000000" + d[l[3]] + d[l[2]] + "111" + d[l[1]] + "0110011";
