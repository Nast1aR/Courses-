class Price:
    exchange_rates = {"USD": 37.8}

    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)
        else:
            return self._convert_and_operate(other, operation="add")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Price(self.amount - other.amount, self.currency)
        else:
            return self._convert_and_operate(other, operation="subtract")

    def _convert_and_operate(self, other, operation):
        if self.currency == "USD":
            converted_amount = (
                other.amount / Price.exchange_rates[other.currency]
            )
        else:
            converted_amount = (
                self.amount * Price.exchange_rates[self.currency]
            )
            if other.currency != "USD":
                converted_amount /= Price.exchange_rates[other.currency]

        if operation == "add":
            return Price(self.amount + converted_amount, self.currency)
        elif operation == "subtract":
            return Price(self.amount - converted_amount, self.currency)

    @staticmethod
    def set_exchange_rate(currency: str, rate: float):
        Price.exchange_rates[currency] = rate


Price.set_exchange_rate("EUR", 41.2)
price1 = Price(100, "USD")
price2 = Price(50, "EUR")


result1 = price1 + price2


print(result1.amount, result1.currency)
