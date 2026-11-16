from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class ModuleSequence:
    sequence_id: int
    subject_id: int
    name_fr: str
    name_en: str
    description_fr: str = ''
    description_en: str = ''
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["ModuleSequence"]
