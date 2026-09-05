"""
입력
정수 1개가 입력된다.
-2147483648 ~ +2147483647, 단 0은 입력되지 않는다.

출력
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력한다.

"""
a = int(input())

if a<0 and a%2 == 0 :
    print("A")
elif a<0 and a%2 == 1:
    print("B") 
elif a>0 and a%2 == 0:
    print("C") 
elif a>0 and a%2 == 1:
    print("D") 