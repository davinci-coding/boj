a = 3
for i in range(5):
    print("%.3f%%" % (a / 5))
    a += 1
# print문에는 자동으로 마지막에 \n(줄넘김) 이 포함
# end= 'a', 줄 넘김이 되지 않고 마지막에 a가 추가
# 