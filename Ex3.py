from fractions import Fraction


def enter_fraction():
    while (True):
        res = input()
        char = "/"
        if char in res:
            list = res.split("/")
            if len(list) == 2:
                if int(list[0]) > 0 and int(list[1]) > 0:
                    int_list = []
                    try:
                        for elem in list:
                            int_list.append(int(elem))
                        return int_list
                    except ValueError:
                        print("That's not a number!")
                else:
                    print("Fractions must be positive!")
            else:
                print("There are more or less than 2 numbers in fraction!")
        else:
            print("You must enter 'int/int' format!")


def greatest_CD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a+b)


def sum_fraction(fraction_1, fraction_2):
    numerator = fraction_1[0]*fraction_2[1] + fraction_1[1]*fraction_2[0]
    denominator = fraction_1[1]*fraction_2[1]
    gcd = greatest_CD(numerator, denominator)
    sum_list = []
    sum_list.append(int(numerator/gcd))
    sum_list.append(int(denominator/gcd))
    return sum_list


def mult_fraction(fraction_1, fraction_2):
    numerator = fraction_1[0]*fraction_2[0]
    denominator = fraction_1[1]*fraction_2[1]
    gcd = greatest_CD(numerator, denominator)
    mult_list = []
    mult_list.append(int(numerator/gcd))
    mult_list.append(int(denominator/gcd))
    return mult_list


print("Enter first fraction:")
fraction_1 = enter_fraction()
print("Enter second fraction:")
fraction_2 = enter_fraction()

sum_list = sum_fraction(fraction_1, fraction_2)
sum_answer = ""
if sum_list[0]//sum_list[1] > 0:
    sum_answer += str(sum_list[0]//sum_list[1]) + " "
    sum_list[0] = sum_list[0] % sum_list[1]
sum_answer += str(sum_list[0])+"/"+str(sum_list[1])
print("Sum:" + sum_answer)
check_sum = Fraction(fraction_1[0], fraction_1[1]) + \
    Fraction(fraction_2[0], fraction_2[1])
print("Check:")
print(check_sum)
print("-------------------------")

mult_list = mult_fraction(fraction_1, fraction_2)
mult_answer = ""
if mult_list[0]//mult_list[1] > 0:
    mult_answer += str(mult_list[0]//mult_list[1]) + " "
    mult_list[0] = mult_list[0] % mult_list[1]
mult_answer += str(mult_list[0])+"/"+str(mult_list[1])
print("Mult:" + mult_answer)
check_mult = Fraction(fraction_1[0], fraction_1[1]) * \
    Fraction(fraction_2[0], fraction_2[1])
print("Check:")
print(check_mult)
