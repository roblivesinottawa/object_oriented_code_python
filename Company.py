class Company:
    def __init__(self, name, turnover, revenue, number_employees):
        self.name = name
        self.turnover = turnover
        self.revenue = revenue
        self.number_employees = number_employees

    def productivity(self):
        return self.revenue / self.number_employees

    def __str__(self):
        return f"The company {self.name} has a turnover of {self.turnover}, a revenue of {self.revenue} and {self.number_employees} employees."

bank = Company("Central City Bank", 5000, 1000000, 100)
print(f"The productivity of the bank is {bank.productivity()}")
print(bank)