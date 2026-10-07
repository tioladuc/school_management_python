from dataclasses import dataclass

@dataclass(frozen=True)
class UserInDto:
    company_code: int
    school_id: str
    profile: str
    username: str
    password: str
