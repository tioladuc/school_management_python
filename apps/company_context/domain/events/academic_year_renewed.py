from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class AcademicYearRenewed:
    company_id: int
    school_id: int
    academic_year_id: int
    renewal_date: date
