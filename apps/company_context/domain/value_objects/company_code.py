from dataclasses import dataclass
import re
from ..exceptions import ValidationError

@dataclass(frozen=True)
class CompanyCode:
    value: str

    def __post_init__(self):
        value = self.value.strip().upper()
        if not re.fullmatch(r'[A-Z0-9][A-Z0-9_-]{1,49}', value):
            raise ValidationError('Company code must be 2-50 characters: letters, numbers, _ or -.')
        object.__setattr__(self, 'value', value)
