import pdb

inputfile = open('day_4.txt')
text = inputfile.read()
inputfile.close()

split = text.split('\n')
split.pop()

print(split)
total = 0

for x in split:
	#print(x[-6:-1])
	letters = x[0:-7]
	number = letters[-3:]

pdb.set_trace()