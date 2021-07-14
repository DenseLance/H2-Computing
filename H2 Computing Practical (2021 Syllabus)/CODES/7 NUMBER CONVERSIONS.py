from random import randint

denary = randint(1000000, 10000000000)
print("Denary:", denary)

## For memorisation purposes
def convert_denary_to_base_16(denary):
    mappings = "0123456789ABCDEF"
    result = ""
    while denary:
        result = mappings[denary % 16] + result
        denary //= 16
    return result

base_16 = convert_denary_to_base_16(denary)
print("Base 16:", base_16)

def convert_base_16_to_denary(base_16):
    mappings = list("0123456789ABCDEF")
    result = 0
    count = 0
    while base_16:
        result += mappings.index(base_16[-1]) * (16 ** count)
        base_16 = base_16[:-1]
        count += 1
    return result

final_denary = convert_base_16_to_denary(base_16)
print("Final denary:", final_denary)

##decimal = randint(1000, 1000000)
##print("Original Number:", decimal)
##
##def convert_decimal_to_base(decimal, base):
##    if base < 2 or base > 36:
##        return None
##    if decimal != int(decimal):
##        return None
##    if decimal == 0:
##        return "0"
##    encodings = [chr(i) for i in range(48, 58)] + \
##                [chr(i) for i in range(65, 91)]
##    
##    result = ""
##    while decimal:
##        result = encodings[decimal % base] + result
##        decimal //= base
##    return result
##
##enc = convert_decimal_to_base(decimal, 32)
##print(enc)
##
##def convert_base_to_decimal(enc, base):
##    if base < 2 or base > 36:
##        return None
##    if type(enc) != str:
##        return None
##    encodings = [chr(i) for i in range(48, 58)] + \
##                [chr(i) for i in range(65, 91)]
##    decodings = dict(zip(encodings, [i for i in range(len(encodings))]))
##    
##    result = 0
##    count = 0
##    while enc:
##        result += decodings[enc[-1]] * (base ** count)
##        enc = enc[:-1]
##        count += 1
##    return result
##
##dec = convert_base_to_decimal(enc, 32)
##print(dec)
