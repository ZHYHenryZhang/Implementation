# That Sinking Feeling
""" input: M,N,R,S
"""
M = 3
N = 2
R = 3
S = 3

""" data structure:
1. array of the board
2. array of all the ships
"""


def shotresult(allships, shot):
    """ input: array of location of all ship, pisition of hit
        return: score """
    score = 0
    # print(allships)
    for item in allships:
        if shot[0] == item[0] and shot[1] == item[1]:
            allships.remove(item)
            return 1000
        else:
            newscore = 1000 - 100 * ( abs(shot[0] - item[0]) + abs( shot[1] - item[1]))
            if newscore > score:
                score = newscore
    return score

allships = [[1,2],[1,1],[0,0]]
allshots = [[0,0],[1,1],[0,1]]
myscore = 0 
hit = 0
shootcount = 0
for item in allshots:
    score = shotresult(allships,item)
    myscore += score
    if score == 1000:
        hit += 1
    shootcount += 1
    # print(item, myscore)
print("{}/{}, score: {}".format(hit,shootcount, myscore))