x = 3
y = 4

mul1 = 3 * 3
mul2 = 5 * 4

def sum(mul1, mul2):
    return mul1 + mul2

result = sum(mul1, mul2)
print("The sum is:", result)

# ---- Second Half: Pay Calculator -----
hours = float(input("Please enter hours worked:"))
hourly_rate = float(input("Please enter pay rate:"))

if hours <=40:
    regular_pay = hours * hourly_rate
    overtime_pay = 0
else:
    regular_pay = 40 * hourly_rate
    overtime_pay = (hours - 40) * hourly_rate * 1.5

total_pay = regular_pay + overtime_pay

print("Regular Pay: $", regular_pay)
print("Overtime Pay: $", overtime_pay)
print("Total Pay: $", total_pay)