# 1041번 주사위
# https://www.acmicpc.net/problem/1041

"""
주사위로 N * N * N의 정육면체를 만들 때 노출되는 면의 숫자의 합을 최소로 하는 문제
노출되는 면을 최소로 하기 위해서는 모서리는 3면, 다른 부분은 2면의 수를 최소로 하면 된다.
주사위는 한 면을 기준으로 반대 면을 제외하고는 모두 인접해 있다.
반대 면을 제외한 숫자들로 최소가 되는 3개의 숫자를 구하여 노출되는 주사위의 개수만큼 계산
"""
