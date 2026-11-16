from ...domain.entities.book_category import BookCategory


class BookCategoryMapper:

    @staticmethod
    def to_domain(m):
        return BookCategory(
            id=m.id,
            school_id=m.school_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.book_category_model import BookCategoryModel
            m = BookCategoryModel()

        m.school_id = e.school_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.status = e.status

        return m
