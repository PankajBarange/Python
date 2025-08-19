even =0
odd=0
for i in range(1,11):
    if i%2==0:
        even+=i
    else:
        odd +=i

print(f"Even Sum is {even}")
print(f"Odd Sum is {odd}")