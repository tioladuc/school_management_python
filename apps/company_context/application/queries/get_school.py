from dataclasses import dataclass
@dataclass(frozen=True)
class GetSchoolQuery:
    school_id: int
