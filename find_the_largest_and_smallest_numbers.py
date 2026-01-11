max = None
min = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    if max is None:
        max = num
    if min is None:
        min = num
    try:
        num = int(num)
        max = int(max)
        min = int(min)
    except(ValueError):
        print("Invalid input")
        continue
    if num > max:
        max = num
    if num < min:
        min = num

print("Maximum is", max)
print("Minimum is", min)
