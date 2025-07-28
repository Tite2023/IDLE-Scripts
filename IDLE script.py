def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

a = 2
b = 3
result = greater_than(a, b)
print("The statement", a, "is greater than", b, "is", str(result).lower())

a = 10
b = 6
result = greater_than(a, b)
print("The statement", a, "is greater than", b, "is", str(result).lower())
