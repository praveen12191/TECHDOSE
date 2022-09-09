def flip(a,pos):
    return a^(1<<pos-1) 
a = int(input())
pos = int(input())
print(bin(flip(a,pos)))