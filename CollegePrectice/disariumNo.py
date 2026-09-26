# Disarium number=89=8*1+9*2=8+81=89

n=int(input("Enter the any number:"))
temp=n
count=0
while(n>0):
  n=n//10
  count=count+1

n=temp
sum=0
while(n>0):
  b=n%10
  sum=sum+(b**count)
  count=count-1
  n=n//10
if(sum==temp):
    print("Disarium Number")
else:
    print("Not Disarium Number") 