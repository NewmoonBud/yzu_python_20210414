# x*y=z
# 1*1=1  1*2=2 .... 1*9=9

x=1
for y in range(1, 10):
    z = x * y
    print("%02d*%02d=%02d" % (x, y, z), end=" ")
print()
print()
print()



# x*y=z
# 9*1=9  9*2=18 .... 9*9=81

for x in range(1, 10):
    for y in range(1, 10):
        z = x * y
        print("%02d*%02d=%02d" % (x, y, z), end=" ")
    print()
print()
print()
print()



# x*y=z
# 9*1=9  9*2=18 .... 9*9=81

n = int(input('請輸入乘法表 size:')) + 1
for x in range(1, n):
    for y in range(1, n):
        z = x * y
        print("%2d*%2d=%3d" % (x, y, z), end=" ")
    print()
print()
print()
print()



# x*y=z
# 9*1=9  9*2=18 .... 9*9=81

n = int(input('請輸入乘法表 size:')) + 1
for x in range(1, n):
    for y in range(1, n):
        z = x * y
        print("%02d*%02d=%03d" % (x, y, z), end=" ")
    print()
print()
print()
print()


# x*y=z
# 9*1=9  9*2=18 .... 9*9=81

n = int(input('請輸入乘法表 size:')) + 1
for x in range(1, n):
    for y in range(1, n):
        z = x * y
        print("%-2d*%-2d=%3d" % (x, y, z), end=" ")
    print()
print()
print()
print()