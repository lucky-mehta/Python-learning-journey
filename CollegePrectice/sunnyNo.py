

n = int(input("Enter a number: "))
x = n + 1
root = int(x ** 0.5)
if root * root == x:
    print("Sunny Number")
else:
    print("Not a Sunny Number")