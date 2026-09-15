n=int(input("Enter the any number:"))
mul=1
while(n>0):
  i=n%10
  mul=mul*i
  n=n//10
  print("Product of digit is:",mul)