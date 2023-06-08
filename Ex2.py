while (True):
    res = input("Enter your number: ")
    try:
        num = int(res)
        break
    except ValueError:
        print("That's not a number!")
list = []
print(hex(num))
while num > 0:
    rem = num % 16
    if rem < 10:
        list.append(rem)
    else:
        match rem:
            case 10:
                list.append("A")
            case 11:
                list.append("B")
            case 12:
                list.append("C")
            case 13:
                list.append("D")
            case 14:
                list.append("E")
            case 15:
                list.append("F")
    num = num//16
list.reverse()
string = ""
for elem in list:
    string += str(elem)
print(string)
