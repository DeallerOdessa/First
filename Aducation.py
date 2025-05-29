num = int(input("Enter a five-digit number: "))

n1 = num % 10
num = num // 10

n2 = num % 10
num = num // 10

n3 = num % 10
num = num // 10

n4 = num % 10
num = num // 10

n5 = num % 10
new_number = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5

print("result:", new_number)