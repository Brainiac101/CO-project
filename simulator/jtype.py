def binary_to_decimal(binary):
    if binary[0] == '1':
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        decimal = -inverted_decimal
    else:
        decimal = int(binary, 2)
    return decimal


def jal(s,d,pc):
    d[s[-12:-9:]]= pc + 4
    pc+= binary_to_decimal(s[0]+s[-20:-12:]+s[-21]+s[-31:-21:]+'0')
    return d,pc



def check(s,d,pc):
    if s[-7::]=="1101111":
        return jal(s,d,pc)

    else:
        return d,pc
