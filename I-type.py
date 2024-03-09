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
    

def lw(l, dict):
    return decimal_to_twos_complement(int(l[2])) + dict[l[3].rstrip(")")] + "010" + dict[l[1]] + "0000011"
def addi(l, dict):
    return decimal_to_twos_complement(int(l[3])) + dict[l[2]] + "000" + dict[l[1]] + "0010011"
def sltiu(l, dict):
    return decimal_to_twos_complement(int(l[3])) + dict[l[2]] + "011" + dict[l[1]] + "0010011"
def jalr(l, dict):
    return decimal_to_twos_complement(int(l[3])) + dict[l[2]] + "000" + dict[l[1]] + "1100111"
