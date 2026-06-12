while True:
    try:
        num = int(input("Give me the rol: "))
        break
    except:
        print("You must enter an integer.")

reversed_num = []
copy = num
while copy / 10 != 0:
    digit = copy % 10
    reversed_num.append(digit)
    copy = copy // 10

index = 0
length = len(reversed_num)
while True:
    for i in range(2, 8):
        if index == length:
            break
        reversed_num[index] = reversed_num[index] * i
        index += 1
    if index == length:
        break

module_11 = sum(reversed_num) % 11
substract = 11 - module_11
verification_digit = num - substract
print(verification_digit)
