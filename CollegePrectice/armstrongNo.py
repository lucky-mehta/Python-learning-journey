n = int(input("Enter any number: "))

temp = n
count = len(str(n))
sum = 0

while (n > 0):
    digit = n % 10
    sum = sum + digit ** count
    n = n // 10

if (sum == temp):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")