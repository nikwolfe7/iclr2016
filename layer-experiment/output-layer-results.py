import sys
import os
def debug(var):
	print(var)
	input("Press Enter...")
	
fname = sys.argv[1]
f = [l.strip() for l in open(fname).readlines()]
pattern = 'Picking the winner...'
spattern = 'Sorting by ground truth, gain, and second gain...'
count = 0
g = []
gl = []
ga = []
sp = []
l1count = 50
l2count = 50
for i in range(len(f)):
	line = f[i]
	if spattern in line:
		spattern = 'OFF...'
		test = f[i+5]
		if test.startswith('E(o1):'):
			accuracy = f[i+4].split()[-1]
			sp.append(accuracy)
	if pattern in line:
		spattern = 'spattern'
		count += 1
		val = int(f[i+1].split()[2])
		g.append(val)
		if val > 50:
			l2count -= 1
			s = "2."+str(l2count).zfill(2)
			gl.append(s)
		else:
			l1count -= 1
			s = "1."+str(l1count).zfill(2)
			gl.append(s)
		if l1count <= 0: l1count = 50
		if l2count <= 0: l2count = 50
		l = f[i+2]
		accuracy = f[i+5]
		if l.startswith('Writing error/gain'):
			lt = f[i+415]
			if lt.startswith('Now training network...'):lt = f[i+6]
			print(lt)
			accuracy = lt
		print(accuracy)
		ga.append(float(accuracy.strip().split()[1]))

print(len(gl))	
gt = g[0:100]
g1 = g[100:200]
g2 = g[200:300]

gta = ga[0:100]
g1a = ga[100:200]
g2a = ga[200:300]

gtl = gl[0:100]
g1l = gl[100:200]
g2l = gl[200:300]

spgt = sp[0:100]
spg1 = sp[100:200]
spg2 = sp[200:300]

o1 = open(fname.rstrip('.txt') + '.neuron-rankings.txt','w')
o2 = open(fname.rstrip('.txt') + '.neuron-accuracy.txt','w')
o3 = open(fname.rstrip('.txt') + '.layer-ids.txt','w')
o4 = open(fname.rstrip('.txt') + '.sp.neuron-accuracy.txt','w')
for i in range(len(gt)):
	o1.write(','.join((str(gt[i]),str(g1[i]),str(g2[i]))) + '\n')
	o2.write(','.join((str(gta[i]),str(g1a[i]),str(g2a[i]))) + '\n')
	o3.write(','.join((str(gtl[i]),str(g1l[i]),str(g2l[i]))) + '\n')
	o4.write(','.join((str(spgt[i]),str(spg1[i]),str(spg2[i]))) + '\n')
o1.close()
o2.close()	
o3.close()	
o4.close()
print("count: " + str(count))
