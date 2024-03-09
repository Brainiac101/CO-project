def decimal_to_twos_complement(decimal_num):
    if decimal_num < 0:
        abs_decimal = abs(decimal_num)
        complement = 2**21 - abs_decimal
    else:
        complement = decimal_num

    twos = bin(complement)[2:]
    
    if len(twos) < 21:
        twos = '0' * (21 - len(twos)) + twos

    return twos
    

def lw(l, d):
    return decimal_to_twos_complement(int(l[2])) + d[l[3].rstrip(")")] + "010" + d[l[1]] + "0000011"
