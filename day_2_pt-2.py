inputfile = open('day_2.txt')
text = inputfile.read()
inputfile.close()

li = text.split(
	)

buttons = [['x','x','5','x','x',],['x','A','6','2','x'],['D','B','7','3','1'],['x','C','8','4','x'],['x','x','9','x','x']]

x = 0
y = 2

for thing in li:
	for char in thing:
		orix = x
		oriy = y
		if char == 'U' and y+1<5:
			y +=1
		if char == 'D' and y-1>-1:
			y -=1
		if char == 'R' and x+1<5: 
			x +=1
		if char == 'L' and x-1>-1:
			x -=1
		if buttons[x][y] == 'x':
			x = orix
			y = oriy
	print (buttons[x][y])
