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

#12 consider a binary file employee.dat containing details such as 
# empno:ename:salary(separator ':') write a python function to display details of those
# employees who are earning between 20000 and 30000(both values inclusive).
'''import pickle
f=open("employee.dat","ab+")
employee=[]
eno=int(input("Enter number:"))
for i in range(eno):
    empno=int(input("Employee no :"))
    ename=input("Employee name :")
    salary=int(input("salary :"))
    p=[empno,ename,salary]
    n=employee.append(p)
    pickle.dump(n,f)'''
'''try:
    while True:
        j=pickle.load(f)
        if j[3]>=20000 and j[3]<=30000:
            print(j,sep=":")
except EOFError:
    f.close()'''
'''
import pickle
def Readfile():
    i = open("employee.dat","rb+")
    try:
        while True:
            x=pickle.load(i)
            
            if float(x[2])>=20000 and float(x[2])<=30000:
                print(i)
    except EOFError:
        print("mmm")
        i.close()
Readfile()'''

#13
'''import pickle
def countrec():
    count = 0
    f = open("STUDENT.dat", "rb")
    while True:
        t = pickle.load(f)
        if t[2]>33:
             count=count+1
             print(t)
        print("Number student with per  greater than 33%", count)'''
'''def disp_rec(a):
    f = open("STUDENT.dat", "rb")
    while True:
        t = pickle.load(f)
        if t[0][0]==a:
            print(t)
g=input("Enter a letter:")
disp_rec(g)'''

#14
'''import pickle
def CountRec(company):
    f=open("store.dat","rb")
    p=[]
    h={}
    try:
        while True:
            g=pickle.load(f)
            p.append(g)
    except EOFError:
        for i in p:
            if i[2] in h:
                h[i[2]]=h[i[2]]+1
            else:
                h[i[2]]=1
        n=h.items()
        for i in n:
            if i[0]==company:
                print('Company name:',i[0],"Count",i[1])
    f.close()
def AddRecord(list):
    f=open("store.dat","wb")
    g=pickle.dump(list,f)
    f.close()'''

#15/16     Write a program to use methods  ReadCSV(UserName) and WriteCSV() to include username and password as some entries for a  CSV file “mydata.csv” and display them.
'''import csv
def WriteCSV():
    fh=open("mydata.csv","w",newline="")
    crd=csv.writer(fh)
    g=int(input("Enter the number of data to be entered: "))
    for i in range(g):
        un=input("Enter UserName:-")
        ps=input("Enter Password:-")
        s=[un,ps]
        crd.writerow(s)
def ReadCSV(rr):
    fh=open("mydata.csv","r")
    crd=csv.reader(fh)
    for i in crd:
        if i[0]==rr:
            print(i[0],":",i[1])
WriteCSV()
s=input("Enter the username to be searched for:-")
ReadCSV(s)'''

#17 Write a Python program using Binarysearch( List , Element ) to search an element from a list.

'''def binary_search(list1, n):
  low = 0
  high = len(list1) - 1
  mid = 0

  while low <= high:
    # for get integer result
    mid = (high + low) // 2

    # Check if n is present at mid
    if list1[mid] < n:
      low = mid + 1

      # If n is greater, compare to the right of mid
    elif list1[mid] > n:
      high = mid - 1

      # If n is smaller, compared to the left of mid
    else:
      return mid
lst=[1,6,10,15,22,80,127]
n=int(input("Enter the number to be searched: "))
s=binary_search(lst, n)
print("The position is",s)'''

#18 bubble sort
'''lst=[11,243,24,11,2,34]
print("Original list is:",lst)
n=len(lst)
for i in range(n):
  for j in range(0,n-i-1):
    if lst[j]>lst[j+1]:
      lst[j],lst[j+1]=lst[j+1],lst[j]
print("List after sorting:",lst)'''

#19 insertion sort
'''lst=[1,22,2,12,442,122]
print("Original list is:",lst)
for i in range(1,len(lst)):
  key=lst[i]
  j=i-1
  while j>=0 and key<lst[j]:
    lst[j+1]=lst[j]
    j=j-1
  else:
    lst[j+1]=key
print("List after sorting:",lst)'''

#20
'''def linear_Search(list1, n, key):
  for i in range(0, n):
    if (list1[i] == key):
      return i
  return -1


list1 = [1, 3, 5, 4, 7, 9]
key =4

n = len(list1)
res = linear_Search(list1, n, key)
if (res == -1):
  print("Element not found")
else:
  print("Element found at index: ", res)'''

#21
lst=[]
'''def isempty(book):
  if book==[]:
    return True
  else:
    return False
def PushOn(tbook,book):
  tbook.append(book)
def pop(tbook):
  if isempty(tbook):
    print("Error:-stack underflow")
  else:
    tbook.pop()'''

#22 (i)
'''def AddCustomer(customer,name):
  customer.append(name)
  top=len(customer)-1
  for a in range(top-1,-1,-1):
    print(customer[a])

#22 (ii)
def RemoveCustomer(cust):
  if cust==[]:
    print("The stack is empty")
  else:
    n,p=cust.pop()
    return "CID:-",n,"Name:-",p'''

#23
'''host=[ ]

ch='y'

def push(host):

  hn=int(input("Enter hostel number"))

  ts=int(input("Enter Total students"))

  tr=int(input("Enter total rooms"))

  temp=[hn,ts,tr]

  host.append(temp)

def pop(host):

  if(host==[]):

      print("No Record")

  else:

      print("Deleted Record is :",host.pop())

def display(host):

  l=len(host)

  print("Hostel Number:Total Students:Total Rooms")

  for i in range(l-1,-1,-1):

      print(host[i][0],":",host[i][1],":",host[i][2])

while(ch=='y' or ch=='Y'):

  print("1. Add Record\n")

  print("2. Delete Record\n")

  print("3. Display Record\n")

  print("4. Exit")

  op=int(input("Enter the Choice"))

  if(op==1):

      push(host)

  elif(op==2):

      pop(host)

  elif(op==3):

      display(host)

  elif(op==4):

      break
  else:

       ch=input("Do you want to enter more(Y/N)")'''

#24
'''def isempty(lst):
    if lst==[]:
        return True
    else:
        return False
def push(lst,ele):
    lst.append(ele)
def pop(lst):
    if isempty(lst):
        print("the stack is empty")
    else:
        lst.pop()
def display(l):
    if isempty(l):
        print("The stack is empty")
    for i in l:
        print(i,end=",")
g=[]
N=[12,13,34,56,21,79,98,22,35,38]
for i in N:
    if i>33:
        push(g,i)
    else:
        continue
pop(g)
display(g)'''

#25
'''def isempty(l):
  if l==[]:
    return True
  else:
    return False
def PushOn(l,m):
  l.append(m)
def pop(l):
  if isempty(l):
    print("Error:-stack underflow")
  else:
    l.pop()
def display(l):
    if isempty(l):
        print("The stack is empty")
    for i in l[::-1]:
        print(str(i),end=",")
p=[]
n=[3,5,10,13,21,23,45,56,60,78]
for i in n:
    if i%3==0:
        PushOn(p,i)
pop(p)
display(p)
'''

'''def isempty(l):
  if l==[]:
    return True
  else:
    return False
def PushOn(l,m):
  l.append(m)
def pop(l):
  if isempty(l):
    print("Error:-stack underflow")
  else:
    l.pop()
def display(l):
    if isempty(l):
        print("The stack is empty")
    for i in l[::-1]:
        print(str(i),end=",")
p=[]
n=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
for i in n:
    if i%2!=0:
        PushOn(p,i)
pop(p)
display(p)'''
