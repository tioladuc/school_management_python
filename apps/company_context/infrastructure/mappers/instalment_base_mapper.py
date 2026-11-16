from ...domain.entities.instalment_base import InstalmentBase


class InstalmentBaseMapper:

    @staticmethod
    def to_domain(m):
        return InstalmentBase(
            id=m.id,
            instalment_id=m.instalment_id,
            class_room_id=m.class_room_id,
            amount=m.amount,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.instalment_base_model import InstalmentBaseModel
            m = InstalmentBaseModel()

        m.instalment_id = e.instalment_id
        m.class_room_id = e.class_room_id
        m.amount = e.amount
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m
