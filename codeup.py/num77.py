"""
입력
정수 1개가 입력된다.
(0 ~ 100)

출력
1부터 그 수까지 짝수만 합해 출력한다.

"""

a = int(input())

start = 0
total = 0
while start <= a:
    if start%2 == 0 :
        total += start
    start +=1

print(total)
