from ...domain.entities.subject import Subject


class SubjectMapper:

    @staticmethod
    def to_domain(m):
        return Subject(
            id=m.id,
            class_room_id=m.class_room_id,
            subject_group_id=m.subject_group_id,
            yearly_staff_id=m.yearly_staff_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            coeficient=m.coeficient,
            order=m.order,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.subject_model import SubjectModel
            m = SubjectModel()

        m.class_room_id = e.class_room_id
        m.subject_group_id = e.subject_group_id
        m.yearly_staff_id = e.yearly_staff_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.coeficient = e.coeficient
        m.order = e.order
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m
