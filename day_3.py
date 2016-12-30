inputfile = open('day_3.txt')
text = inputfile.read()
inputfile.close()

triangles = [[int(y) for y in x.split()] for x in text.split('\n')]
del triangles[-1]
print(triangles)


poss = 0
for i in triangles:
	i.sort()
	print(i)
	if int(i[0]) + int(i[1]) > int(i[2]):
		poss += 1
print(poss)