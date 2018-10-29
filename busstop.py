# bus stop name shorten
busstop1 = [150, 30, 31 ,41, 42, 101, 39 , 40, 201, 202, 200]
busstop2 = [1, 2, 3, 4, 5, 6, 9, 10, 33, 55, 54, 32]

def shorten(original):
    original.sort()
    print(original)
    end = len(original)

    a = 0 # mark the start
    b = 0 # mark the end

    while a < end: # when the start reaches end of list
        # move the end forward
        b = a + 1 
        old = a
        
        # loop until not satisfy
        while b < end and original[b] == original[old] + 1:
            old = b
            b += 1
        
        # check looping result:
        if original[old] == original[a]: # not consecutive
            print(original[a], end = ", ")
        elif original[old] - original[a] == 1: # only 2 numbers, so does not make it short
            print("{}, {}".format(original[a], original[old]), end = ", ")
        else:
            print("{}-{}".format(original[a],original[old]),end = ", ")

        # let start catch up with end
        a = b

    print(" ") # format

shorten(busstop1)
shorten(busstop2)

# original confusing one, not tested, buggy
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