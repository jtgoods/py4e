text = "X-DSPAM-Confidence:    0.8475"
zero = text.find("0")
num = float(text[zero:])
print(num)
