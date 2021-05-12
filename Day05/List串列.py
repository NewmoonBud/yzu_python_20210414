# 數組: List(元素可重複), set(元素不可重複), dict(key/value的組合元素) 三種
scores = [ 100, 90, 80]   # List
scores.append(70)
print(scores)
print(scores[1])  # 取得維度 = 1 的資料(維度是從0開始)
print(len(scores))    # 取得元素個數
print(scores.index(70))  # 取得某元素的維度值
print(max(scores), min(scores))  # 取得元素最大 最小值

# 走訪每一個元素 I
for x in scores:
    print(x)

# 走訪每一個元素(含元素值) II
for (idx, value) in enumerate(scores):
    print(idx, value)
