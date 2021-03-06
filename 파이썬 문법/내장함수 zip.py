'''zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.'''

print( list(zip([1, 2, 3], [4, 5, 6])) )
# [(1, 4), (2, 5), (3, 6)]

print( list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) )
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

print( list(zip("abc", "def")) )
# [('a', 'd'), ('b', 'e'), ('c', 'f')]




'''zip은 배열을 같은 인덱스끼리 짝지어준다. 
하지만 배열의 길이가 다를 경우 같은 인덱스끼리만 짝지어주고, zip 객체에서 나머지 인덱스는 제외된다.'''

a = [1,2,3,4,5]
b = [1,2,3,4]
zip(a,b) # zip(a,b)를 shell에 찍으면 객체 <zip object at 0x104a3e960>가 나옴 

for t in zip(a,b):
    print(t)

# a의 마지막 인덱스 5는 제외되어 있는 것을 알 수 있다.
# (1, 1)
# (2, 2)
# (3, 3)
# (4, 4)
