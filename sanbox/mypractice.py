print([num for num in [4, 2, 6, 8, 10] if num % 2 == 0])


people = ["Charlie", "Casey", "Cody", "Carly", "Christina"]
print(all([name[0] == "C" for name in people]))
print([name[0] == "C" for name in people])

nums = [2, 61, 50, 78, 12]
print(all([num % 2 == 0 for num in nums]))

print(any([num % 2 == 0 for num in nums]))

for x in reversed(range(0, 10)):
    print(x)


def count():
    result = []
    for x in reversed(range(1, 11)):
        result.append(x)
    return result


print(count())
