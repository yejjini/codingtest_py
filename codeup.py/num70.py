"""
입력
월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)

출력
계절 이름을 출력한다.

월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

"""
month = int(input())

if month==12 or 1<=month<=2:
    print("winter")
elif 3<=month<=5:
    print("spring")
elif 6<= month<=8:
    print("summer")
elif 9<=month<=11:
    print("fall")