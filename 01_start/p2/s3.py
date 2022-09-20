def Bit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (i << j) else "0"
    print(output)

a = 0x86
key = 0xAA

print(a)

print("a>", end='')
Bit_print(a)

print("a^=key >", end='')
a ^= key ;
Bit_print(a)