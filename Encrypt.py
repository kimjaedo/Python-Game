# 사용할 아스키 범위 - 이 범위를 벗어나면 오류가 발생할 수 있습니다.
asciiMin = 32
asciiMax = 126

# 암호화 키
key = 314159
key = str(key)

# 암호화할 메시지 입력받기
message = input("암호화할 메시지를 입력하세요: ")

# 암호화 메시지용 변수 초기화하기
messEncr = ""

# 메시지 루프
for index in range(0, len(message)):
    char = ord(message[index])
    if char < asciiMin or char > asciiMax:
        messEncr += message[index]
    else:
        ascNum = char + int(key[index % len(key)])
        if ascNum > asciiMax:
            ascNum -= (asciiMax - asciiMin)
        messEncr = messEncr + chr(ascNum)

print("암호화한 메시지:", messEncr)