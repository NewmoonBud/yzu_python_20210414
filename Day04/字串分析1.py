str = ' she sell sea shell on the sea shore '
print(str)
print('字串長度:', len(str))
print('字串有幾個s:', str.count('s'))
print('字串on這個字的位置:',str.find('on'))
print('字串off這個字的位置:',str.find('off'))
print('字串有無sea這個字:','有' if str.find('sea') >= 0 else '沒有')
print('字串有無land這個字:','有' if str.find('land') >= 0 else '沒有')
print('字串有幾個英文單字:', str.count(' ')+1)

# 去除左右空白
str = str.strip()   # 去除左右空白
str = str.lstrip()  # 去除左空白
str = str.rstrip()  # 去除右空白
print('字串有幾個英文單字:', str.count(' ')+1)

# 是否都是英文字(a-z, A-Z)
print('字串是否都是英文字:', str.isalpha())

# #小技巧: 先利用 replace將中間空白去除
print('字串是否都是英文字:', str.replace(' ', '').isalpha())

print(str[2])
print(str[-2])
print(str[0:3])  # 取出0-3的字串，但不含3，即 0 - 2

path = 'c:\temp\nba\score.py'
print('路徑位置:', path)

path = r'c:\temp\nba\score.py'  # 字串包含特殊碼, ex: \, 的處理技巧 加 r
print('路徑位置:', path)






