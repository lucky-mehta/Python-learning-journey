fruit="Mango"
print(fruit)
mangolen=len(fruit)
print(mangolen)        #total length of string
print(fruit[0:4])      # including 0 but not 4
print(fruit[1:4])      #including 1 but not 4
print(fruit[:5])       #:5 means index 0 to (5-1)index


print(fruit[0:-3])
print(fruit[:len(fruit)-3])     #index 0 to (5-3)

print(fruit[-1:len(fruit)-3])    #(5-1=4)to index (5-3=2)  so this is the wrong

print(fruit[-3:-1])