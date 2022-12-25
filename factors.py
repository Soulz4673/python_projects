import math

#factor singles
n = int(input("Please enter a positive integer: "))
factors = [x for x in range(1, n + 1) if n % x == 0]
print("Factors of", n, ":", factors)

#factor pairs
n1 = int(input("Please enter a positive integer: "))
factors1 = [(x, n1//x) for x in range(1, n1 + 1) if n1 % x == 0]
print("Factor pairs of", n1, ":", factors1)

#unique factor pairs
n2 = int(input("Please enter a positive integer: "))
factors2 = [(x, n2//x) for x in range(1, round(math.sqrt(n2)) + 1) if n2 % x == 0]
print("Factor pairs of", n2, ":", factors2)
