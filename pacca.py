#1
'''def COUNTNOW(PLACES):
    for i in PLACES:
        if len(i)>7:
            print(i)
COUNTNOW(["MELBORN","TOKYO","BEIZING","PINKCITY","SUNCITY"])'''
#2
'''def countmy():
    fh=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\DATA.txt")
    n=fh.read()
    count=0
    for i in n.split():
        if i=="my":
            count=count+1
    print('"my" occurs',count,"times")
    fh.close()
countmy()'''
#3
'''def displaylines():
    fh=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\MYNOTES.txt")
    n=fh.readlines()
    for i in n:
        if i[0]=='K':
            print(i,end="")
    fh.close()
displaylines()'''
#4
'''f1=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\source.txt")
f2=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\target.txt",'w')
n=f1.readlines()
for i in n:
    if i[0]=='@':
        f2.write(i)
f1.close()
f2.close()'''
#5
'''def SRCount():
    fh=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\STORY.txt")
    count=0
    n=fh.read()
    for i in n.split():
        for j in range(len(i)):
            if i[j]=="S" or i[j]=="s" or i[j]=="R" or i[j]=="r":
                count+=1
    print("The alphabets S and R(including s and r) occur",count,"times")
    fh.close()
SRCount()'''
#6
'''def Display():
    fh=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\XYZ.txt")
    n=fh.read()
    for i in n.split():
        if len(i)>=3:
            print(i)
Display()'''
#7
'''def count_is_as():
    f=open('C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\STORY.txt')
    count=0
    n=f.read()
    for i in n.split():
        if i=='is' or i=='as':
            count=count+1
    print("as & is occurs",count,"times")
    f.close()
count_is_as()'''
#8
'''fh=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\XYZ.txt")
lowercase=uppercase=vowels=consonants=0
n=fh.read()
count=0
for i in n:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        vowels=vowels+1
    else:
        consonants=consonants+1
    if i.isupper():
        uppercase=uppercase+1
    if i.islower():
        lowercase=lowercase+1
print("no. of vowels",vowels)
print("no. of consonants",consonants)
print("no. of uppercase",uppercase)
print("no. of lowercase",lowercase)'''

#9
'''f1=open('C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\STORY.txt')
f2=open('C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\New file.txt','w')
n=f1.readlines()
for i in n:
    if 'a' in i:
        continue
    else:
        f2.write(i)
f1.close()
f2.close()'''

#10
'''import pickle
stu={}
stufile=open('C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\Mera.dat','wb')
p=int(input("no of students: "))
for i in range(p):
    rno=int(input("Enter roll no."))
    name=input("Enter name:")
    stu['Rollno']=rno
    stu['Name']=name
    pickle.dump(stu,stufile)
stufile.close()
sf=open('C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\Mera.dat','rb')
rn=int(input("enter a roll to be searched: "))

try:
    found=False
    while True:
        n=pickle.load(sf)
        if n["Rollno"]==rn:
            print("The child is",n["Name"])
            found=True
            break
except EOFError:
    if found==False:
        print("No found")
    else:
        print("Found!")
    sf.close()'''
'''
#12 consider a binary file employee.dat containing details such as 
# empno:ename:salary(separator ':') write a python function to display details of those
# employees who are earning between 20000 and 30000(both values inclusive).
import pickle
f=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\employee.dat","wb+")
employee=[]
eno=int(input("Enter number:"))
for i in range(eno):
    empno=int(input("Employee no :"))
    ename=input("Employee name :")
    salary=int(input("salary :"))
    p=[empno,ename,salary]
    n=employee.append(p)
    pickle.dump(n,f)
try:
    while True:
        j=pickle.load(f)
        if j[3]>=20000 and j[3]<=30000:
            print(j,sep=":")
except EOFError:
    f.close()
'''
f=open("C:\\Users\\LENOVO\\Desktop\\Ye walla pacca\\employee.dat","rb+")
def Readfile():
    i = open("employee.dat","rb+")
    x = i.readline()
    while(x):
        I = x.split(':')
        if (20000>=float(I[2])<=30000):
            print(x)
            x = i.readline()
