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
