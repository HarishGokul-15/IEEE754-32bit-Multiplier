a_operand = '01000000011000000000000000000000'
b_operand = '01000000100000000000000000000000'
print(a_operand, '-', b_operand)
sign = int(a_operand[0]) ^ int(b_operand[0])
a_exponent = a_operand[1:9]

b_exponent = b_operand[1:9]
for i in range(len(a_exponent)):
    if i == 0:
        and_a = int(a_exponent[i]) & int(a_exponent[i+1])
    if i == 1:
        continue

    else:
        and_a = int(and_a) & int(a_exponent[i])

for i in range(len(a_exponent)):
    if i == 0:
        and_b = int(b_exponent[i]) & int(b_exponent[i+1])
    if i == 1:
        continue
    else:
        and_b = and_b & int(b_exponent[i])

exception_ = and_a | and_b

for i in range(len(a_exponent)):
    if i ==0:
        or_a = int(a_exponent[i]) | int(a_exponent[i+1])
    if i == 1:
        continue
    else:
        or_a = or_a | int(a_exponent[i])

for i in range(len(b_exponent)):
    if i == 0:
        or_b = int(b_exponent[i]) | int(b_exponent[i+1])
    if i == 1:
        continue
    else:
        or_b = or_b | int(b_exponent[i])

if or_a:
    a = "1" + a_operand[9:32]
else:
    a = "0" + a_operand[9:32]

if or_b:
    b = "1" + b_operand[9:32]
else:
    b = "0" + b_operand[9:32]
print(b)
product = bin(((int(a, 2)) * (int(b, 2))))
print(product)
if len(product[2:]) < 48:
        # Add leading zeroes to the input string to make it 9 bits long
    product = "{:0>48}".format(product[2:])
    product = '0b'+product
print((len(product)))
product_round = 0
print((product[25:51]))
last_product = product[25:51]
print("hg", (last_product))
for i in range(len(product[25:51])):
    if i == 0:
        product_round = int(last_product[i], 2) | int(last_product[i+1], 2)
    if i == 1:
        continue
    else:
        product_round = product_round | int(last_product[i])

if product[2] == "1":
    normalised = 1
else:
    normalised = 0

if normalised == 1:
    product_normalised = product
else:
    product_normalised = bin((int(product, 2)) << 1)

product_sample = (int(product_normalised[26], 2)) & (product_round)
print(type(product_normalised[26]))
product_mantissa_ = int(product_normalised[3:26], 2) + (product_sample)
# convert back to binary string with leading zeros
product_mantissa = format(product_mantissa_, "0" + str(len(product_normalised[3:26])) + "b")
print(product_mantissa)
zero = 1 if exception_ else 1 if (
product_mantissa == "00000000000000000000000") else 0
sum_exponent = bin(int(a_exponent, 2) + int(b_exponent, 2))
exponent = int(sum_exponent, 2) - 127 + (normalised)
exponent_bin = bin(exponent)
print(exponent_bin[2:])
if len(exponent_bin[2:]) < 9:
        # Add leading zeroes to the input string to make it 9 bits long
    exponent_bin = "{:0>9}".format(exponent_bin[2:])
print(exponent_bin)

overflow = ((int(exponent_bin[0], 2) & ~(int(exponent_bin[1], 2))) & ~(int(str(zero), 2)))

if ((int(exponent_bin[0], 2) & int(exponent_bin[1], 2)) & ~int(str(zero), 2)):
    underflow = 1
else:
    underflow = 0
print(str(exponent_bin))
if exception_:
    result = "00000000000000000000000000000000"
elif (zero):
    result = str(sign)+"0000000000000000000000000000000"
elif (overflow):
    result = str(sign) + "11111111" + "00000000000000000000000"
elif (underflow):
    result = str(sign) + "0000000000000000000000000000000"
else:
    result = str(sign) + str((exponent_bin[1:])) + product_mantissa
print((result))
