def bd(binary):
    if binary[0] == '1':
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        decimal = -inverted_decimal
    else:
        decimal = int(binary, 2)

    return decimal

def decimal_to_hexadecimal(decimal_num):
    hexnum = hex(decimal_num)
    hexnum = hexnum[2:]
    hexnum = hexnum.zfill(8)
    hexnum = '0x' + hexnum
    return hexnum

def sw(s,d,datamem):
    imm=20*s[0]+s[-32:-25]+s[-12:-7]
    mem=decimal_to_hexadecimal(bd(s[-20:-15])+(bd(imm)))
    datamem[mem]=d[s[-25:-20]]
    return datamem

def check(s, d,datamem):
    if s[17:20]=="010":
        datamem=sw(s, d,datamem)





