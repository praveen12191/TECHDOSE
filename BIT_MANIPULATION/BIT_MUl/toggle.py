def toggle(s):
    return chr(ord(s)^32)
s = input().strip()
print(toggle(s))