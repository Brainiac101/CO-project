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
    

def auipc(l, d):
    x=decimal_to_twos_complement(int(l[2]))
    return x[-32:-12:] + "0010111"
def lui(l, d):
    x=decimal_to_twos_complement(int(l[2]))
    return x[-32:-12:] + "0110111" 
