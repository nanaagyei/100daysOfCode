print("This program only finds the sum of multiples of three and five for n consecutive integers")
n=input("Please the number of consecutive integers: ")
total = 0
for i in range(1, n+1):
    if i//3==0 or i//5==0:
        total += i
print(total)
