# 調查有五位同學身高與體重如下
import statistics as stat
h = [172, 168, 164, 170, 176]  # cm
w = [62, 57, 58, 64, 64]   # Kg

# 問該學生身高與體重的分散程度哪一個大，要用 變異系數 = 標準差 / 算術平均
# 變異係數 c.v. = sd(標準差) / avg(平均)
h_cv = stat.stdev(h)/stat.mean(h)
w_cv = stat.stdev(w)/stat.mean(w)
print('身高 cv:', '%.2f%%' % (h_cv * 100))
print('體重 cv:', '%.2f%%' % (w_cv * 100))
print('體重 cv:', w_cv * 100, '%')



