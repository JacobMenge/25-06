print("=== 11 ===")

for i in range(11):
    print(i)

print("=== 5,11 ===")

for i in range(1,11):
    print(i)

print("=== 1,11,2 ===")

for i in range(1,11,2):
    print(i)


namen = ["Anna", "Ben", "Lia"]

print(enumerate(namen))

for index, name in enumerate(namen):
    print(index, name)



for buchstabe in "Python":
    print(buchstabe)
