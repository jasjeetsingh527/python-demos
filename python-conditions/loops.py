from datetime import datetime

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
    break
else:
    print("Done")


# Break, Continue, Pass
for i in range(10):
    if i == 5:
        print("Skipping 5")
        continue  # Skip the rest of the loop for this iteration
    elif i == 8:
        print("Breaking at 8")
        break  # Exit the loop entirely
    else:
        print(f"Current number: {i}")


# Exercise
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


# my solution
start_time1 = datetime.now()
for items in picture:
    i = 0
    picture_list = []
    while i < len(items):
        picture_list.insert(i, "*" if items[i] == 1 else " ")
        i += 1
    print("".join(picture_list))

end_time1 = datetime.now()

print((end_time1 - start_time1) * 1000)

# another way around
start_time1 = datetime.now()
for row in picture:
    for pixel in row:
        p = "*" if pixel else " "
        print(p, end="")
    print("")
end_time1 = datetime.now()
print((end_time1 - start_time1) * 1000)

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicate_list = []
processed_list = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate_list:
            duplicate_list.append(item)

print(f"duplicate letters: {", ".join(duplicate_list)}")
