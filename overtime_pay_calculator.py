hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h >= 40:
    new_r = 1.5 * r
    print(40 * r + (h-40) * new_r)
else:
    print(h * r)
