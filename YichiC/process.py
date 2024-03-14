infile = 'input.txt'
outfile = 'output.txt'

d = None

with open(infile, 'r') as f:
	d = f.read()
	d = d.split(' ')
	d = [int(x) for x in d]

	print(d)
	
with open(outfile, 'w') as f:
	for x in d:
		f.write(str(x) + '\n')


