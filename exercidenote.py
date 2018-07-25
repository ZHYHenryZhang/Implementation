# sum function for sum a list
list_a = [1,2,3,4,5]
sum_list_a = sum(list_a) 
print(sum_list_a)

# zip function for iterate together
list_b = [5,4,3,2,1]
score_a = 0
score_b = 0
for temp_x, temp_y in zip(list_a,list_b):
    if temp_x > temp_y:
        score_a += 1
    elif temp_x < temp_y:
        score_b += 1
print(score_a, score_b)

# range function
def diagonalDifference(arr):
    diag_a = 0
    diag_b = 0
    i = 0
    j = 0
    for i in range(0,len(arr[0])):
        for j in range(0,len(arr[0])):
            if(i == j):
                diag_a += arr[i][j]
            if(i+j == len(arr[0])-1):
                diag_b += arr[i][j]
    return abs(diag_a - diag_b)

print("exercise 5")
arr_5 = [[1,2,3],[4,5,6],[7,8,9]]
print(range(0,3))
print(len(arr_5[0]))
print(diagonalDifference(arr_5))


def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    for x in arr:
        if x > 0:
            pos_count += 1
        elif x < 0:
            neg_count += 1
        else:
            zero_count += 1
    sum_count = pos_count + neg_count + zero_count
    print(pos_count/sum_count)
    print(neg_count/sum_count)
    print(zero_count/sum_count)

print("exercise 6")
arr_5 = [-2,3,4,0,-1,2]
plusMinus(arr_5)

# print with end specified end=""
# print function in python
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
def staircase(n):
    for i in range(0,n):
        for j in range(0,n):
            if j + i < n-1:
                print(" ",end="")
            else:
                print("#",end="")
        if i + j < 2 * n - 1:
            print(" ")

print("exercise 7")
staircase(6)

# sorted function
def miniMaxSum(arr):
    min_arr = arr[0]
    max_arr = arr[0]
    for x in arr:
        if x < min_arr:
            min_arr = x
        if x > max_arr:
            max_arr = x
    sum_arr = sum(arr)
    print(sum_arr - max_arr,sum_arr - min_arr)

    

print("exercise 8")
arr_8 = [1,2,3,5,6,7]
print(miniMaxSum(arr_8))

# method by other people
# ar = sorted(map(int, input().split()))
# print(sum(ar[:-1]), sum(ar[1:]))


def birthdayCakeCandles(ar):
    max = ar[0]
    max_count = 0
    for x in ar:
        if x > max:
            max_count = 0
            max = x
        if x == max:
            max_count += 1
    return max_count

print("exercise 9")
arr_9 = [ 2,3,4,5,5,5,5,2]

# short version
print(arr_9.count(max(arr_9)))
print(birthdayCakeCandles(arr_9))


# str() to convert to string
# str.zfill(n) to fill zero in front of string
# map() to do a function to each element of a sequence
# string.[i:j] to get part of string
# string.split("symbol") to split string with the symbol
def timeConversion(s):
    # import string
    hh,mm,ss=map(int,s[0:-2].split(":"))
    if hh == 12:
        hh -= 12
    if  s[-2]=='P':
        hh += 12
    return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":"+str(ss).zfill(2)

str_10 = "12:00:00AM"
print(str_10, timeConversion(str_10))
# print(':'.join(map(lambda x: str(x).rjust(2, '0'), time_list)))
# n = 123
# s = '%05d' % n
# assert s == '00123'

    