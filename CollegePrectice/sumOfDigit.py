n=int(input("Enter the any number:"))
sum=0
while(n>0):
  i=n%10
  sum=sum+i
  n=n//10
  print("Sum of digit is:",sum)