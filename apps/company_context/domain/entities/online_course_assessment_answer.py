from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class OnlineCourseAssessmentAnswer:
    online_course_assessment_id: int
    yearly_staff_id: int
    name_fr: str
    name_en: str
    description_fr: str = ''
    description_en: str = ''
    file_path: str
    status: str = 'ACTIVE'
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by_id: int
    update_by_id: int
    id: int | None = None

__all__ = ["OnlineCourseAssessmentAnswer"]
