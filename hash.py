
import hashlib
import sys
import random

f = int(input('input 1 or 2 or 3: '))
l = []
if f == 1:
	f = int(input('kol-vo: '))
	for i in range(0, f):
		hsh = hashlib.md5(str(random.randrange(1, 10000000)).encode("utf")).hexdigest()
		print(hsh)
		l.append(hsh)
elif f == 2:
	f = input('pass: ')
	hsh = hashlib.md5(f.encode("utf")).hexdigest()
	print(hsh)
	l.append(hsh)
elif f == 3:
	fff = open(input('filename: '), 'r')
	for i in fff:
		hsh = hashlib.md5(i.encode("utf")).hexdigest()
		print(hsh)
		l.append(hsh)
	fff.close()
ff = open('hash.txt', 'w')
for i in l:
	ff.write(i + '\n')
ff.close()