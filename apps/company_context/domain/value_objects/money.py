from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from ..exceptions import ValidationError

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str = 'CAD'

    def __post_init__(self):
        amount = Decimal(self.amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        currency = self.currency.upper()
        if amount < 0:
            raise ValidationError('Money amount cannot be negative.')
        if len(currency) != 3:
            raise ValidationError('Currency must be a 3-letter ISO code.')
        object.__setattr__(self, 'amount', amount)
        object.__setattr__(self, 'currency', currency)

    def multiply(self, quantity):
        return Money(self.amount * Decimal(quantity), self.currency)
