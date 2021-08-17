number = int(input())
word = input()

# write a condition for plurals
if number == 1:
    print(number, word)
if number != 1:
    word = word + "s"
    print(number, word)
