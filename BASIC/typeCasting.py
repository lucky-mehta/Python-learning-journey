
# explicit typecating-we manually converted one datatype to another
# 1st example
a="2"
b="4"
print(a+b)
print(int(a)+int(b))

# 2nd example

string="50"
number=6
abc=int(string)
sum=number+abc
print("The sum of both number is:",sum)


# implicit typecasting-python automatically convert the datatype
c=4.5
d=10
print(c+d)
print("type:",type(c+d))