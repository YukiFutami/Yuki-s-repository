# 1부터 20사이의 수 중에서 3의 배수도 아니고 짝수도 아닌 수만 출력하는 프로그램

# for 또는 while중 어느 것을 사용하기

# 반복문 구현
# 1부터 20까지의 정수를 순화하는 반복문을 구현하기
for count_value in range(1, 21):
    
    # 조건 필터링
    # 3의 배수도 아니고 짝수도 아닌 수만을 출력하기
    if not count_value % 3 == 0 and not count_value % 2 == 0 :
        print(count_value)

