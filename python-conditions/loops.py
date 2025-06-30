a = "this is a string"
b = [1, 2, 3, 4, 5]
c = {1, 2, 3, 4, 5}
d = (1, 2, 3, 4, 5)

e = [a, b, c, d]

for item in e:
    for element in item:
        print(element)


f = {"name": "John Doe", "age": 60, "can_swim": False}
for key, value in f.items():
    print(f"Key: {key} and value: {value}")

i = 0
g = [f, {"name": "Alice Doe", "age": 10, "can_swim": True}]
for items in g:
    i += 1
    print(f"S.No. {i}")
    print(f"name: {items["name"]}")
    print(f"age: {items["age"]}")
    print(f"can swim?: {items["can_swim"]}")
    print("_" * 50)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = 0
for item in my_list:
    total_sum += item

print(f"total of my_list: {total_sum}")


# range:
for _ in range(1, 100):
    print(_)

# enumerate
for i, number in enumerate(list(range(100))):
    print(f"current number: {number}")
    if number == 50:
        print(f"index of number 50 is: {i}")
        break


# WHile loop
i = 0
while i <= 50:
    print(i)
    i += 1
else:
    print("Done")
