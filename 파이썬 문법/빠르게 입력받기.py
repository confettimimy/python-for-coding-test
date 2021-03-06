'''이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
   데이터 개수가 1000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 이진탐색 알고리즘을 고려해보자.
   그런데 이렇게 입력 데이터의 개수가 많은 문제에 input()함수를 사용하면 동작 속도가 느려 시간 초과로 오답 판정을 받을 수 있다.
   이처럼 입력 데이터가 많은 문제는 sys 라이브러리의 readline()함수를 이용하면 시간초과를 피할 수 있다.'''

'''즉, 입력되는 데이터의 수가 많다면 파이썬 내장함수인 input()을 더 빠르게 작동하는 sys.stdin.readline()으로 치환하여 사용하는 것이 좋다.'''
 
import sys


# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
print(input_data)


# 빠르게 입력받기 위해 input()을 sys.stdin.readline()으로 대체해 사용
n, m = map(int, sys.stdin.readline().split())
print(n,m)
 