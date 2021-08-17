deposit = int(input())
year = 0
interest_rate = 7.1 / 100

while deposit < 700000:
    passive_income = deposit * interest_rate
    year += 1
    deposit = deposit + passive_income
print(year)
