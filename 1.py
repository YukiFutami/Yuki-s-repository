# 정수 5개를 입력받아 합계와 평균을 출력하는 프로그램

# 5개 정수를 입력하고 입력받은 정수의 합계를 계산
# total = 0
# for count_value in range(1, 6):
#     number = int(input(f"{count_value}번째 값을 입력하세요: "))
#     total += number

# # 평균 계산
# average = total / 5

# # 결과 출력
# print("합계: ",total)
# print("평균: ",average) 


# 先生の解説

# # 整数５つ入力
# input_1 = int(input("１番目の値を入力せよ: "))
# input_2 = int(input("１番目の値を入力せよ: "))
# input_3 = int(input("１番目の値を入力せよ: "))
# input_4 = int(input("１番目の値を入力せよ: "))
# input_5 = int(input("１番目の値を入力せよ: "))

# # 合計計算
# sum = input_1 + input_2 + input_3 + input_4 + input_5

# # 平均計算
# ave = sum / 5

# # 合計と平均を出力
# print("合計: ",sum)
# print("平均: ",ave) 


total = 0
for count_value in range(1, 5):
    number = int(input(f"{count_value}번째 값을 입력하세요: "))
    total += number

# 평균 계산
average = total / 5

# 결과 출력
print("합계: ",total)
print("평균: ",average) 