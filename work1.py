f = open("num.txt", "r")
a = []#数组
for line in f.readlines():
	a.append(int(line))
n = len(a)
ss = 0
s = []#前缀数组
for i in range(0,n):
	ss += a[i]
	s.append(ss)
small = 65535
big = -65535
for i in range(0,n):
	if s[i] < small:
		small = s[i]
	if s[i] - small > big:
		big = s[i] - small
print big
