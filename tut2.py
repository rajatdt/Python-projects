l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
zip(l1, l2)
print(list(zip(l1, l2)))
m = 'spam'
for (offset, x) in enumerate(m):
	print(x, 'appears at offset', offset)
print(open('tut.py').read())
f = open('tut.py')
for item in f:
	f.readline()
def iterate():
	x = 'spam'
	while x:
		print x
		x = x[1:]
t = 'ham'
if t == 'spam':
	iterate()
else:
	print 'wont iterate because x is not equal to spam'
def times(x, y):
	return x*y
t = times('nano', 4)
print t
def intersect(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
	print res
s1 = [1, 2, 3, 4]
s2 = [7, 8, 5, 6]
intersect(s1, s2)
y = 0
page = open('tut.py').readlines()
for x in page:
	while x:
		y+=1
		break
print y

l = ['1', '2', '3', '4']
for x in range(len(l)):
	l[x] += 'r'
print l

y = 0
f = open('tut.py').readlines()
print 'total lines of code', len(f)
for x in f:
	if x[0] == 'p':
		y+=1
		print x
print 'number of print statements is ', y

import sys
print sys.__doc__

x = 88

def func():
	x = 99
	print x
func()
print x

import tut
print(tut.t)
tut.t = 'ham'
print(tut.t)

import tut
tut.setx(88)
print tut.x

hot = 99
def f1():
	hot = 88
	def f2():
		print hot
	f2()

f1()

file = open('tut.py').readlines()
def file_ops():
	for item in file:
		if not item.startswith('p'):
			print item
	print 'these lines do not have print statements'

file_ops()

def maker(n):
	action = (lambda x: x**n)
	return action

f = maker(2)
print f(24)

def makeAction():
	acts = []
	for i in range(5):
		acts.append(lambda x, i=i: i ** x)
	return acts

acts = makeAction()
print acts[3](2)

def tester(start):
	def nested(label):
		print(label, nested.state)
		nested.state += 1
	nested.state = start
	return nested

f = tester(0)
f('spam')
f('ham')
f('clam')
g = tester(40)
g('rajat')
f('rohit')
g('gaurav')

def multiple(X, L):
	X = 2
	L = [3, 4]
	return X, L

x = 1
l = [1, 2]

x, l = multiple(x, l)
print x, l
