n,m,s,r= [int(x) for x in input().split()]
# n: x, m: y, s: num ships, r: num fires
ships = []
fires = []

for line in range(s):
	ships.append([int(x) for x in input().split()])

for line in range(r):
	fires.append([int(x) for x in input().split()])

# define distance function
def distance(a,b):
	d = abs(a[0] - b[0]) + abs(a[1] - b[1])
	return d

# point = 0
# sunk = 0
# # remove common points from lists
# temp_fires = fires
# for f in temp_fires:
# 	if f in ships:
# 		ships.remove(f)
# 		point += 1000
# 		sunk += 1
# 	else:
# 		distances = []
# 		for sh in ships:
# 			distances.append(distance(f, sh))
# 		point += max(0, 1000 - 100 * min(distances))


# print(ships, fires)

# #  get min dist
# for f in fires:
# 	distances = []
# 	for sh in ships:
# 		distances.append(distance(f, sh))
# 	point += max(0, 1000 - 100 * min(distances))




# calculate points
sunk = 0
point = 0

for i in fires:
	if i in ships:
		point += 1000
		sunk += 1
		ships.remove(i)
		
	else:
		dsum = []
		for ship in ships:
			d = distance(i,ship)
			dsum.append(d)
			
		dfinal = min(dsum)
		point += max(0,1000 - 100*dfinal)



#print results

# ratio = sunk/s

print("{}/{} ships sunk. Score: {} points".format(sunk, s, point))



