number = int(input("번호를 제공해주세요 :"))

if number % 2 == 0:
    print("짝수입니다.")
elif number % 2 == 1:
    print("홀수입니다.")
else:
    print("정수인 숫자를 적어주세요!")