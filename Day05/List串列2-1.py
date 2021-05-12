# 數組: List(元素可重複), set(元素不可重複), dict(key/value的組合元素) 三種
import random as r

scores = [ 100, -10, 90, 80, 999]   # List
# error_score = scores.pop(1)
# print(error_score, scores)
# error_score = scores.pop(3)
# print(error_score, scores)

# 利用 pop() 將不合法的分數挑出by teacher
error_scores = []
for s in scores:
    if s < 0 or s > 100:
        error_scores.append(s)

print(scores)
print(error_scores)
for e in error_scores:
    scores.pop(scores.index(e))

print(scores)


# 反序
scores = [1, 7, 3, 5]
scores.reverse()
print(scores)

#排序
scores.sort()
print(scores)

# 洗牌 (請先 import random as r)
r.shuffle(scores)
print(scores)
