import sys
import os
fname = 'mnist-deep.exp.txt'
f = [l.strip() for l in open(fname).readlines()]
pattern = 'Picking the winner...'
count = 0
g = []
ga = []
for i in range(len(f)):
	line = f[i]
	if pattern in line:
		count += 1
		g.append(int(f[i+1].split()[2]))
		l = f[i+2]
		accuracy = f[i+5]
		if l.startswith('Writing error/gain'):
			lt = f[i+415]
			if lt.startswith('Now training network...'):lt = f[i+6]
			print(lt)
			accuracy = lt
		print(accuracy)
		ga.append(float(accuracy.strip().split()[1]))
	
gt = g[0:100]
g1 = g[100:200]
g2 = g[200:300]

gta = ga[0:100]
g1a = ga[100:200]
g2a = ga[200:300]
o1 = open(fname.strip('.txt') + '.neuron-rankings.txt','w')
o2 = open(fname.strip('.txt') + '.neuron-accuracy.txt','w')
for i in range(len(gt)):
	o1.write(','.join((str(gt[i]),str(g1[i]),str(g2[i]))) + '\n')
	o2.write(','.join((str(gta[i]),str(g1a[i]),str(g2a[i]))) + '\n')
o1.close()
o2.close()	
print("count: " + str(count))
