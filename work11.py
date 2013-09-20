x=raw_input("row number\n")
y=raw_input("line number\n")
f=open("num.txt","r")
num=[]
for i in range(0,int(x)):
    for j in range(0,int(y)):
        l=f.readline()
        l=l.strip('\n').split(",")
        num.append(l)
temp=[0]*int(x)
s=0
a=-1000000
for i in range(0,int(y1)):
    for j in range(i,int(y1)):
        for k in range(0,int(x)):
            temp[k]+=int(num[j][k])
            if(s+temp[k]<temp[k]):
                s=0
            s+=temp[k]
            if(a<s):
                a=s
        s=0
    s=0
    temp=[0]*int(x)
print a
