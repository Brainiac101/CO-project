def binary_to_decimal(binary):
    if binary[0] == '1':
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        decimal = -inverted_decimal
    else:
        decimal = int(binary, 2)
    return decimal



def auipc(s,d,pc):
    d[s[-12:-9:]]= pc + binary_to_decimal(s[-32:-12:]+'0'*12)
    return d

def lui(s,d):
    d[s[-12:-9:]]= binary_to_decimal(s[-32:-12:]+'0'*12)
    return d

def check(s,d,pc):
    if s[-7::]=="0110111":
        return auipc(s,d,pc)
    elif s[-7::]=="0010111":
        return lui(s,d)
    else:
        return d
