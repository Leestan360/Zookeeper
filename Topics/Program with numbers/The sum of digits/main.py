# put your python code here
integer = int(input())

digit_1 = (integer // 100)
digit_2 = ((integer - (digit_1 * 100)) // 10)
digit_3 = (integer % 10)

sum_of_digits = (digit_1 + digit_2 + digit_3)

print(sum_of_digits)
