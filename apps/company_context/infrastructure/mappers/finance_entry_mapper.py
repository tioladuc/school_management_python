from ...domain.entities.finance_entry import FinanceEntry


class FinanceEntryMapper:

    @staticmethod
    def to_domain(m):
        return FinanceEntry(
            id=m.id,
            finance_item_id=m.finance_item_id,
            amount=m.amount,
            deposit_date=m.deposit_date,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
            created_by_id=m.created_by_id,
            update_by_id=m.update_by_id,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.finance_entry_model import FinanceEntryModel
            m = FinanceEntryModel()

        m.finance_item_id = e.finance_item_id
        m.amount = e.amount
        m.deposit_date = e.deposit_date
        m.status = e.status
        m.created_by_id = e.created_by_id
        m.update_by_id = e.update_by_id

        return m
