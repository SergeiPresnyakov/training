def compute_income(deposit, interest_rate, amount_months):
    return deposit * (1 + interest_rate / (12 * 100)) ** amount_months

k = 5  # percent
n = 10  # months
s = 1918

for x in range(1, 100000):
    #вычислить прибыль для вклада x с помощью функции  compute_income(x, ..., ...)
    income = compute_income(x, k, n)
    if round(income) - x == s:
        
       # вывести значение вклада x
       print(x)