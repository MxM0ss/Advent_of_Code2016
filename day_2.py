inputfile = open('day_2.txt')
text = inputfile.read()
inputfile.close()

li = text.split(
	)

numbers = [['7','4','1'],['8','5','2'],['9','6','3']]

x = 1
y = 1
for thing in li:
	for char in thing:
		if char == 'U' and y+1<3:
			y +=1
		if char == 'D' and y-1>-1:
			y -=1
		if char == 'R' and x+1<3: 
			x +=1
		if char == 'L' and x-1>-1:
			x -=1
	print (numbers[x][y])

