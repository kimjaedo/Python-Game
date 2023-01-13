import random

# 컴퓨터 하나 고르기
cChoice = random.choice("SRP")

# 사용자 선택 얻기
print("가위, 바위, 보?")
uChoice = input("S(가위), R(바위), P(보) 중 하나를 고르세요: ")

# 테스트하기
print("여러분: ", uChoice)
print("컴퓨터: ", cChoice)

# 선택 비교하기
if cChoice == uChoice:
    print("무승부입니다!")
elif uChoice == "R" and cChoice =="P":
    print("졌습니다.")
elif uChoice == "P" and cChoice == "R":
    print("이겼습니다.")
elif uChoice == "R" and cChoice == "S":
    print("이겼습니다.")
elif uChoice == "S" and cChoice == "R":
    print("졌습니다.")
elif uChoice == "P" and cChoice == "S":
    print("졌습니다.")
elif uChoice =="S" and cChoice == "P":
    print("이겼습니다.")
else:
    print("게임 설명을 또 듣는 일은 지겨울 겁니다. 그렇죠?")