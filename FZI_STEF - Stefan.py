# https://pl.spoj.com/problems/FZI_STEF/
profit = amount = 0
tests = int(input())
for i in range(tests):
    amount = max(0, amount + int(input()))
    profit = max(amount, profit)
print(profit)
