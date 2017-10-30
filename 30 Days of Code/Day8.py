phoneBook ={}
n = int(input().strip())
for _ in range(n):
    name, number = input().split()
    phoneBook[name]=number


ns = input().strip()

try:
    while True:
        if(ns in phoneBook.keys()):
            print("=".join([ns,phoneBook[ns]]))
        else:
            print("Not found")
        ns = input().strip()
except:
    pass