inputfile = open("day_1.txt")
text = inputfile.read()
inputfile.close()


instructions = text.split(', ')

x = 0
y = 0
print(x,y)

face = 'n'
for direct in instructions:
	if face == 'n':
		if direct[0] == 'R':
			x = x + int(direct.strip('RL'))
			face = 'e'
		elif direct[0] == 'L':
			x = x - int(direct.strip('RL'))
			face = 'w'
	elif face == 's':
		if direct[0] == 'R':
			x = x - int(direct.strip('RL'))
			face = 'w'
		elif direct[0] == 'L':
			x = x + int(direct.strip('RL'))
			face = 'e'
	elif face == 'e':
		if direct[0] == 'R':
			y = y - int(direct.strip('RL'))
			face = 's'
		elif direct[0] == 'L':
			y = y + int(direct.strip('RL'))
			face = 'n'
	else:
		if direct[0] == 'R':
			y = y + int(direct.strip('RL'))
			face = 'n'
		elif direct[0] == 'L':
			y = y - int(direct.strip('RL'))
			face = 's'

print(x,y)
