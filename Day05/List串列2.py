# 數組: List(元素可重複), set(元素不可重複), dict(key/value的組合元素) 三種
scores = [ 100, -10, 90, 80, 999]   # List
# error_score = scores.pop(1)
# print(error_score, scores)
# error_score = scores.pop(3)
# print(error_score, scores)

# 利用 pop() 將不合法的分數挑出by me
for (idx, value) in enumerate(scores):
    if value < 0:
        print(idx, value)

# 利用 pop() 將不合法的分數挑出by teacher
for s in scores:
    if s < 0 or s > 100:
        error_score = scores.pop(scores.index(s))
        print("不合法分數:", error_score)
        print(scores)


scores1 = [ 100, -10, -20, 90, -80, 999]
for s in scores1:
    if s < 0 or s > 100:
        error_score = scores1.pop(scores1.index(s))
        print("不合法分數:", error_score)
        print(scores1)
