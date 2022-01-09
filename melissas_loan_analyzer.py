# coding: utf-8
import csv
from pathlib import Path


loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print(f"The number of loans is : {number_of_loans}.")

loan_total = sum(loan_costs)
print(f"The sum of the loan costs total: ${loan_total}.")

average_loan_price = loan_total / number_of_loans
print(f"The average loan price of all 5 loans is: ${average_loan_price}.")


loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
print(f"The future value of the loan is: ${future_value}.")
remaining_months = loan.get("remaining_months")
print(f"The remaining months left on the loan is: {remaining_months}")

annual_discount_rate = .2
present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
print(f"The present value of the loan is: {present_value:.2f}.")

cost = loan.get("loan_price")
if present_value >= cost:
    print("Yes, the loan is worth at least the cost to buy it.")
else:
    print("No, the loan is too expensive and not worth the price")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
annual_discount_rate = .2
def calculate_present_value(future_value, remaining_months, annual_discout_rate):
    present_value = future_value / (1+(annual_discount_rate / 12)) ** remaining_months
    return present_value

present_value = calculate_present_value(new_loan.get("future_value"), new_loan["remaining_months"], 0.20)
print(f"The present value of the loan is: {present_value:.2f}")


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans = []
for loan in loans:
    if loan["loan_price"] <= 500:
        print(inexpensive_loans)
        inexpensive_loans.append(loan)
        print(inexpensive_loans)
print(f"The inexpensive loans are as follows: {inexpensive_loans}")

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")

with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

