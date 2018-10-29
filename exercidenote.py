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

def gradingStudents(grades):
    #
    # Write your code here.
    #
    for x in range(len(grades)):
        if grades[x] > 37 and grades[x] % 5 > 2:
            grades[x] = grades[x] + 5 - grades[x] % 5
    return grades

grades_11 = [23, 34, 44, 67, 78, 89]
print("exercise 11")
print(grades_11, gradingStudents(grades_11))
# note that following do not change the item in it
for x in grades_11:
    x = x + 5
print(grades_11)


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    for x in apples:
        if x + a >= s and x + a <= t:
            count_apples += 1
    for y in oranges:
        if y + b >= s and y + b <= t:
            count_oranges += 1
    print(count_apples)
    print(count_oranges)

print("exercise 12")
s_12 = 7
t_12 = 11
a_12 = 5
b_12 = 15
apples = [-4,-2, 0, 2, 3, 4]
oranges = [-7, -6, -5, 0, 2]
countApplesAndOranges(s_12,t_12,a_12,b_12,apples,oranges)
# https://www.hackerrank.com/rest/contests/master/challenges/apple-and-orange/hackers/Jake_Lost/download_solution?primary=true
apple = sum([1 for ap in apples if a_12 + ap >= s_12 and a_12 + ap <= t_12])
orange = sum([1 for ora in oranges if b_12 + ora <= t_12 and b_12 + ora >= s_12])
print(apple)
print(orange)

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            print("YES")
        else:
            print("NO")
    elif (x1 - x2) / (v1 - v2) > 0:
        print("NO")
    else:
        if (x1 - x2) % (v1 - v2) == 0:
            print("YES")
        else:
            print("NO")

print("exercise 13")
x1_13 = 0
v1_13 = 3
x2_13 = 4
v2_13 = 2
kangaroo(x1_13, v1_13, x2_13, v2_13)

def computefactor(a, b):
    if not a == b:
        return computefactor(min(a,b),abs(a-b))
    else:
        return a

def computemultiplier(a ,b):
    return a * b // computefactor(a, b)


def getminmultiplier(a):
    if len(a) == 2:
        return computemultiplier(a[0],a[1])
    elif len(a) > 2:
        return computemultiplier(getminmultiplier(a[:-1]),a[-1])
    else:
        print(" too short ")

def getmaxfactor(a):
    if len(a) == 2:
        return computefactor(a[0],a[1])
    elif len(a) > 2:
        return computefactor(getmaxfactor(a[:-1]),a[-1])
    else:
        print("too short")

def common(a, b, x):
    for m in a:
        if not x % m == 0:
            return False
    for n in b:
        if not n % x == 0:
            return False
    return True

def getTotalX(a, b):
    #
    # Write your code here.
    #
    minmul = getminmultiplier(a)
    maxfac = getmaxfactor(b)
    if minmul > maxfac:
        return 0
    else:
        count = 0
        for x in range(minmul, maxfac+1):
            if common(a,b,x):
                count += 1
        return count

print("exercise 14")
a_14 = [4,4,8]
b_14 = [32, 32, 16]
# print(b_14[:-1],b_14[-1])
print(getTotalX(a_14, b_14))

# print(computefactor(24, 36))
# print(computemultiplier(54,36))
# print(getminmultiplier([24,36,18,54,108]))
s_14 = 12
t_14 = 13
for x_14 in range(s_14, t_14):
    print(x_14, end=", ")
print()
c_14 = [12,18,24,72]
print(getmaxfactor(c_14))

# correct but need improve
# def getTotalX(a, b):
#     #
#     # Write your code here.
#     #
#     minmul = max(a)
#     maxfac = min(b)
#     if minmul > maxfac:
#         return 0
#     else:
#         count = 0
#         for x in range(minmul, maxfac+1):
#             if common(a,b,x):
#                 count += 1
#         return count

# annotation of python
# def gcd(a: int, b: int) -> int:
#     while a % b != 0:
#         a, b = b, (a % b)
#     return b

# def gcd_list(lst: list) -> int:
#     return reduce(gcd, lst)

# import sys
# def lcm(a):
#     if len(a)==1:
#         return a[0]
#     if len(a)==2:
#         return a[0]*a[1]//gcd((a[0],a[1]))
#     return lcm((a[0],lcm(a[1:])))

# def gcd(a):
#     if len(a)==1:
#         return a[0]
#     if len(a)==2:
#         return gcd((a[1],a[0]%a[1])) if a[1]!=0 else a[0] # Euclid's alg
#     return gcd((a[0],gcd(a[1:])))

# input()
# lcm_a = lcm([x for x in map(int,input().strip().split())])
# gcd_b = gcd([x for x in map(int,input().strip().split())])
# print(sum(1 for x in range(lcm_a,gcd_b+1,lcm_a) if gcd_b%x==0))


# lenA, lenB = map(int, raw_input().split())
# setA = map(int, raw_input().split())
# setB = map(int, raw_input().split())

# maxA = max(setA)
# minB = min(setB)
# count = 0
# for num in range(maxA, minB + 1):
#     left = all([num % numA == 0 for numA in setA])
#     right = all([numB % num == 0 for numB in setB])
#     count += left*right
# print count

# n,m = [int(i) for i in input().strip().split(' ')]
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
# b = [int(b_temp) for b_temp in input().strip().split(' ')]

# result = 0
# for x in range(max(a), min(b)+1):
#     divideA = [x%j!=0 for j in a]
#     divideB = [j%x!=0 for j in b]
#     if sum(divideA)==0 and sum(divideB)==0:
#         result += 1
# print(result)


def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0
    for x in scores:
            if x < min_score:
                min_count += 1
                min_score = x
            elif x > max_score:
                max_count += 1
                max_score = x
    return max_count, min_count

print("exercise 15")
scores_15 = [2,4,5,1,9]
results_15 = breakingRecords(scores_15)
print(results_15)


def solve(s, d, m):
    if len(s) < m:
        return 0
    else:
        count = 0
        for x in range(len(s) - m + 1):
            sum = 0
            for y in range(m):
                sum += s[x + y]
            if sum == d:
                count += 1
        return count


s_16 = [1, 2, 1, 3, 2]
d_16 = 3
m_16 = 2
print(solve(s_16, d_16, m_16))