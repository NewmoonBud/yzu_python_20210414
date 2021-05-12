import random as r

ans = r.randint(1, 99)
min = 0
max = 100
count = 5

while count > 0:

    # 倒數猜測的次數
    guess = int(input('(%d). 請輸入 %d ~ %d :' % (count, min, max)))

    # 檢查guess的輸入資料是否在min與max之間
    if guess >= max or guess <= min:
        print('數字範圍錯誤')
        continue

    # 判定結果
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('使用者答對了')
        break

    # 電腦猜
    PC_guess = r.randint(min+1, max-1)
    print('(%d). 電腦猜 %d ~ %d : %d' % (count, min, max, PC_guess))

    # 判定電腦結果
    if PC_guess > ans:
        max = PC_guess
    elif PC_guess < ans:
        min = PC_guess
    else:
        print('電腦答對了')
        break

    # 將count -1
    count = count - 1
