n = int(input("Enter number of values : "))

l = []
for val in range(0,n,1):
    num= int(input("Enter integer : "))
    l.append(num)


print("Circulating the elements of list ", l)
   
for val in range(0,n,1):
    num = l.pop(0)
    l.append(num)
    print(l)
