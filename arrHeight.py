'''
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
'''

'''
1 ≤ array의 길이 ≤ 100
1 ≤ height ≤ 200
1 ≤ array의 원소 ≤ 200
'''

'''
array	                height	result
[149, 180, 192, 170]	167	     3
[180, 120, 140]	        190	     0
'''

'''
입출력 예 #1

149, 180, 192, 170 중 머쓱이보다 키가 큰 사람은 180, 192, 170으로 세 명입니다.
입출력 예 #2

180, 120, 140 중 190보다 큰 수는 없으므로 0명입니다.
''' 
import numpy as np 


def solution(arrHeight, height):

    # np.array() 함수를 사용하여 a라는 np 배열 생성
    a = np.array(arrHeight) 

    # 비교연산하여 true 개수 확인하기
    answer = np.count_nonzero(a > height)
    '''
    # boolean 타입 배열로 출력 후, 트루개수 확인하기 
    answer = a > height
    print(f"answer: {answer}")   |   결과 : [False  True  True  True]
    '''
    return answer

a = solution([149, 180, 192, 170], 167)
print(a)