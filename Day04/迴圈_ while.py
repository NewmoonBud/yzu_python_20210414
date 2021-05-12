import random as r
while True:
    n = r.randint(1, 100)
    if n % 3 == 0:
        print(n)
    if n == 50:
        print('離開迴圈, n =', n)
        break

while True:
    n = r.randint(1, 100)
    if n % 3 == 0:
        print(n)
        continue   # 直接跳回while，此次continue以下的程式碼不執行
    if n == 50:
        print('離開迴圈, n =', n)
        break  # 強制跳離迴圈



