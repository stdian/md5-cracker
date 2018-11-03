
#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import sys
import time
import string

symbols = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], [], [], ['!', '@', '"', "'", '#', '№', '$', ';', '%', '^', ':', '&', '?', '*', '(', ')', '-', '_', '=', '+', '|', '/', ',', '<', '>'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '"', "'", '#', '№', '$', ';', '%', '^', ':', '&', '?', '*', '(', ')', '-', '_', '=', '+', '|', '/', ',', '<', '>']]

for c in string.ascii_lowercase:
	symbols[1].append(c)
	symbols[4].append(c)

for c in string.ascii_uppercase:
	symbols[2].append(c)
	symbols[4].append(c)

wsimbols = []
tt = 0
hashss = open('hash.txt', 'r')
hashs = []

for strr in hashss:
	hashs.append(strr)
hashs = [line.rstrip() for line in hashs]

iii = -1
f = 0
ch = 0
hshforprint = []
slova = []

def checkhash(passs):
	global iii
	global ch
	global hashs

	haw = hashlib.md5()
	haw = str(hashlib.md5(passs.encode("utf-8")).hexdigest())
	iii += 1

	for hshs in hashs:
		if hshs == haw:
			sys.stdout.write('\r\r' + (str(iii) + '    ' + passs + '                                                                ') + '')
			print()
			ch += 1
			print('Hash ' + hshs + ' cracked. \nThe password: ' + passs)
			hshforprint.append(hshs + ' - ' + passs)
			if ch == len(hashs):
				print('Result:')
				for i in hshforprint:
					print(i)
				saveresults()
				exit()
			else:
				saveresults()
		else:
			sys.stdout.write('\r\r' + (str(iii) + '    ' + passs + '                                                                ') + '')

def saveresults():
	fff = open('result.txt', 'w')
	for i in hshforprint:
		fff.write(i + '\n')
	print('Time elapsed: ' + str(round(time.clock() - tt)))	
	fff.write('Time elapsed: ' + str(round(time.clock() - tt)))
	fff.close()
	print('Check Result.txt')

def generatepasswordswithslovar():
	global slova
	slova.append('-')
	slova.append('_')

	do = ''
	time.sleep(0.05)
	print('write "stop" to stop entering words')
	while do != 'stop':
		do = input('word: ')
		if do != 'stop':
			slova.append(do)

	passes = []
	global iii

	for i in range(0, len(slova)):
		checkhash(slova[i])
		for j in range(0, len(slova)):
			checkhash(slova[i] + slova[j])
			for k in range(0, len(slova)):
				checkhash(slova[i] + slova[j] + slova[k])
				for l in range(0, len(slova)):
					checkhash(slova[i] + slova[j] + slova[k] + slova[l])
					for ll in range(0, len(slova)):
						checkhash(slova[i] + slova[j] + slova[k] + slova[l] + slova[ll])

def generatepasswithmask():
	global tt
	ch = 0
	print('Read me:')
	time.sleep(0.05)
	print('n - numbers\ns - lowercase letters\nb - uppercase letters\nc - special symbols\na - all')
	time.sleep(0.05)
	print('example: n?s?s?c')
	time.sleep(0.05)
	print('max password length 20 symbols')
	time.sleep(0.05)
	mask = input('input mask: ')
	mask = mask.split('?')
	passes = []

	for i in mask:
		if i == 'n':
			wsimbols.append(symbols[0])
		if i == 's':
			wsimbols.append(symbols[1])
		if i == 'b':
			wsimbols.append(symbols[2])
		if i == 'c':
			wsimbols.append(symbols[3])
		if i == 'a':
			wsimbols.append(symbols[4])
	l = len(wsimbols)

	tt = time.clock()		
	if l >= 1:
		for w in wsimbols[0]:
			checkhash(w)
			if l >= 2:
				for ww in wsimbols[1]:
					checkhash(w + ww)
					if l >= 3:
						for www in wsimbols[2]:
							checkhash(w + ww + www)
							if l >= 4:
								for wwww in wsimbols[3]:
									checkhash(w + ww + www + wwww)
									if l >= 5:
										for wwwww in wsimbols[4]:
											checkhash(w + ww + www + wwww + wwwww)
											if l >= 6:
												for v in wsimbols[5]:
													checkhash(w + ww + www + wwww + wwwww + v)
													if l >= 7:
														for vv in wsimbols[6]:
															checkhash(w + ww + www + wwww + wwwww + v + vv)
															if l >= 8:
																for vvv in wsimbols[7]:
																	checkhash(w + ww + www + wwww + wwwww + v + vv + vvv)
																	if l >= 9:
																		for vvvv in wsimbols[8]:
																			checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv)
																			if l >= 10:
																				for vvvvv in wsimbols[9]:
																					checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv)
																					if l >= 11:
																						for q in wsimbols[10]:
																							checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q)
																							if l >= 12:
																								for qq in wsimbols[11]:
																									checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq)
																									if l >= 13:
																										for qqq in wsimbols[12]:
																											checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq)
																											if l >= 14:
																												for qqqq in wsimbols[13]:
																													checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq + qqqq)
																													if l >= 15:
																														checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq + qqqq + qqqqq)
																														if l >= 16:
																															for e in wsimbols[15]:
																																checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq + qqqq + qqqqq + e)
																																if l >= 17:
																																	for ee in wsimbols[16]:
																																		checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq + qqqq + qqqqq + e + ee)
																																		if l >= 18:
																																			for eee in wsimbols[17]:
																																				checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq + qqqq + qqqqq + e + ee + eee)
																																				if l >= 19:
																																					for eeee in wsimbols[18]:
																																						checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq + qqqq + qqqqq + e + ee + eee + eeee)
																																						if l >= 20:
																																							for eeeee in wsimbols[19]:
																																								checkhash(w + ww + www + wwww + wwwww + v + vv + vvv + vvvv + vvvvv + q + qq + qqq + qqqq + qqqqq + e + ee + eee + eeee + eeeee)
																						
	print('Time elapsed: ' + str(round(time.clock() - tt)))		
	exit()

print('hello!')
time.sleep(0.2)
print("it's cracker passwords programm")
time.sleep(0.2)
print("What's type of your password?")
time.sleep(0.05)
print('1. use numbers.txt')
time.sleep(0.05)
print('2. use rockyou.txt')
time.sleep(0.05)
print('3. use custom dictionary')
time.sleep(0.05)
print('4. generate passwords')
time.sleep(0.05)
print('5. crack password with mask')
time.sleep(0.05)
print('6. exit')
time.sleep(0.05)
do = int(input('input: '))
if do == 1:
	f = open('numbers.txt', 'r')
	time.sleep(0.2)
	print('chose numbers.txt')
elif do == 2:
	f = open('rockyou.txt', 'r')
	time.sleep(0.2)
	print('chose rockyou.txt')
elif do == 3:
	t = input('filename: ')
	f = open(t, 'r')
	time.sleep(0.2)
	print('chose ' + t)	
elif do == 4:
	generatepasswordswithslovar()
	time.sleep(0.2)
elif do == 5:
	generatepasswithmask()	
	time.sleep(0.2)	
elif do == 6:
	exit()
else:
	print('Incorrect choose!')
	exit()

rr = []
if f != 0:
	for strr in f:
		rr.append(strr)
	rr = [line.rstrip() for line in rr]	

i = -1
tt = time.clock()
for pwd in rr:
	checkhash(pwd)
print('Time elapsed: ' + str(round(time.clock() - tt)))		