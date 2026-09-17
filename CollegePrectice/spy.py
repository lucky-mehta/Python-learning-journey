# sum of digit is equal to product of digit is called spy number.
n=int(input("Enter the any number:"))
sum=0
mul=1
while(n>0):
    i=n%10
    sum=sum+i
    mul=mul*i
    n=n//10

if(sum==mul):
    print("Spy Number")
else:
    print("Not Spy Number")