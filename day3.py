print("This program helps add n consecutive integers starting from 1")
x=input("Please enter the number of consecutive integers you want to add: ")
total = 0
for i in range(1,x+1):
    total += i
print("The sum of " + str(x) + " consecutive numbers is " + str(total)) 