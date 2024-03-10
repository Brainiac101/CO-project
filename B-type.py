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
def beq(l,d):
    return decimal_to_twos_complement(int(l[3]))[19]+" "+decimal_to_twos_complement(int(l[3]))[21:27]+" " + d[l[2]] + d[l[1]] + "000" + " "+decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20]+" "+ "1100011";

def bne(l,d):
    return  decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27]+ d[l[2]] + d[l[1]] + "001" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def blt(l,d):
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "100" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def bge(l,d):
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "101" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def bltu(l,d):
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "110" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

def bgeu(l,d):
    return decimal_to_twos_complement(int(l[3]))[19]+decimal_to_twos_complement(int(l[3]))[21:27] + d[l[2]] + d[l[1]] + "111" +  decimal_to_twos_complement(int(l[3]))[27:31] + decimal_to_twos_complement(int(l[3]))[20] + "1100011";

