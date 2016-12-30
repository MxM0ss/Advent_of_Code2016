inputfile = open('day_3.txt')
text = inputfile.read()
inputfile.close()

tri = text.split()
new = []

import pdb; pdb.set_trace()

while len(tri) > 0:
	new.append(int(tri.pop(0)))
	new.append(int(tri.pop(2)))
	new.append(int(tri.pop(4)))
	new.append(int(tri.pop(0)))
	new.append(int(tri.pop(1)))
	new.append(int(tri.pop(2)))
	new.append(int(tri.pop(0)))
	new.append(int(tri.pop(0)))
	new.append(int(tri.pop(0)))


i=0
newtri = []
while i < len(new):
	newtri.append(new[i:i+3])
	i+=3
print(newtri)



poss = 0
for i in newtri:
	i.sort()
	print(i)
	if int(i[0]) + int(i[1]) > int(i[2]):
		poss += 1
print(poss)









