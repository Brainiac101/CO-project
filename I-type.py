def decimal_to_twos_complement(decimal_num):
    if decimal_num < 0:
        abs_decimal = abs(decimal_num)
        complement = 2**12 - abs_decimal
    else:
        complement = decimal_num

    twos = bin(complement)[2:]
    
    if len(twos) < 12:
        twos = '0' * (12 - len(twos)) + twos

    return twos
    

def lw(l, d):
    return decimal_to_twos_complement(int(l[3])) + d[l[2]] + "010" + d[l[1]] + "0000011"
def addi(l, d):
    return decimal_to_twos_complement(int(l[3])) + d[l[2]] + "000" + d[l[1]] + "0010011"
def sltiu(l, d):
    return decimal_to_twos_complement(int(l[3])) + d[l[2]] + "011" + d[l[1]] + "0010011"
def jalr(l, d):
    return decimal_to_twos_complement(int(l[3])) + d[l[2]] + "000" + d[l[1]] + "1100111"
