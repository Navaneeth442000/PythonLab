#Store a list of first names

li=[]
c=0
a=int(input("Enter the number of names:"))
for i in range (a):
  x=input("Enter first name:")
  li.append(x)
for i in li:
  for j in i:
    if j=="a":
      c=c+1
print("Number of a's :",c)

