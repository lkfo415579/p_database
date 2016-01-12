import numpy
a = numpy.empty((4, 4))

for y in range(1,4):
	for x in range(1,4):
		print str(a[y][x]),
		#print 'x = ' + str(x) + ' y = ' + str(y),
	print ''

for i in range(1,4):
	for j in range(1,4):
		if j>1 and i>1:
			a[i][j] = a[a[i-1][j-1],a[i][j-1]]+1
		else:
			a[i][j] = i*j
		#print str(a[i][j])
'''
for y in range(1,4):
	for x in range(1,4):
		print str(a[y][x]),
		#print 'x = ' + str(x) + ' y = ' + str(y),
	print ''
'''