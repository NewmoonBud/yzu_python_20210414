salary = {'John': 50000, 'Marry' : 60000}  # 此即字典格式
print(salary)
print('John 的薪資:', salary['John'])
for key in salary:
    print("%s 的薪資 %d" % (key, salary[key]))

# 新增元素
salary.setdefault('Bob', 70000)
print(salary)

# 求薪資總和
summ = 0
for add in salary:
    summ = summ + salary[add]

print(summ)

