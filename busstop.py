# bus stop name shorten

original = [150, 30, 31 ,41, 42, 101, 39 , 40, 201, 202, 200]
original.sort()
print(original)
end = len(original)
a = 0
b = 0

while a < end - 1:
    b = a + 1
    old = a
    while b < end and original[b] == original[old] + 1:
        old = b
        b += 1
    if original[old] == original[a]:
        print(original[a], end = ", ")
    elif original[old] - original[a] == 1:
        print("{}, {}".format(original[a], original[old]), end = ", ")
    else:
        print("{}-{}".format(original[a],original[old]),end = ", ")
    a = b

if a == end - 1:
    print(original[a])
print(" ")


""" i += 1
if original[i] == old+1:
    if begin == None:
        begin = old
else:
    if begin != None:
        print("{}-{}".format(begin, old), end = "")
        begin = None
    else:
        print("{}".format(old), end = " ")
old = original[i] """