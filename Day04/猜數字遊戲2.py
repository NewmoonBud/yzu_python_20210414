import random as r
ans = r.randint(1, 99)
min = 0
max = 100

while True:
    guess = int(input('請輸入 %d ~ %d : ' % (min, max)))
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
        print('答對了')
        break
