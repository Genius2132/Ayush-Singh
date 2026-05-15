n=int(input("enter a number"))
originalnum=0
count=0
res=0
while n>0:
    n=n//10
    count+=1
n=originalnum
while n>0:
    r=n%10
    res=res+r**count
    n=n//10
if res==originalnum:
   print("it is armstong number")
else:
    print("it is not armstrong number")

