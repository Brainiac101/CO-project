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

def sw(l, dict):
    imm=decimal_to_twos_complement(int(l[2]))
    return imm[:7]+ dict[l[1]] + dict[l[3].rstrip(")")] + "010" + imm[7:] + "0100011"
