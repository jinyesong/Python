chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

students = [chulsu, younghee, yong, minsu]

for scores in students:
    print(scores)

for scores in students:
     total = 0
     for s in scores:
         total = total + s
     average = total / 3
     print(scores, total, round(average,1))

import operator  
for scores in students:
     total = reduce(operator.add, scores)
     average = total / len(scores)
     print(scores, total, average)
