from dataclasses import dataclass

@dataclass(frozen=True)
class UpdateSchoolCommand:
    school_id: int
    name: str
    city: str
    country: str
