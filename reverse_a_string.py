

a = str(input("Enter a word to be reversed: "))

b = list(a)
c = reversed(b)
list_c = list(c)


reversed_a = ""

for i in list_c:
    reversed_a += i
    
print(reversed_a)