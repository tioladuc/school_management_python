from ...domain.entities.book import Book


class BookMapper:

    @staticmethod
    def to_domain(m):
        return Book(
            id=m.id,
            book_category_id=m.book_category_id,
            name_fr=m.name_fr,
            name_en=m.name_en,
            description_fr=m.description_fr,
            description_en=m.description_en,
            author=m.author,
            second_name_fr=m.second_name_fr,
            second_name_en=m.second_name_en,
            published_date=m.published_date,
            published_by=m.published_by,
            illustrated_by=m.illustrated_by,
            keywords=m.keywords,
            quantity=m.quantity,
            status=m.status,
            created_at=m.created_at,
            updated_at=m.updated_at,
        )

    @staticmethod
    def to_model(e, m=None):
        if m is None:
            from ...infrastructure.orm.book_model import BookModel
            m = BookModel()

        m.book_category_id = e.book_category_id
        m.name_fr = e.name_fr
        m.name_en = e.name_en
        m.description_fr = e.description_fr
        m.description_en = e.description_en
        m.author = e.author
        m.second_name_fr = e.second_name_fr
        m.second_name_en = e.second_name_en
        m.published_date = e.published_date
        m.published_by = e.published_by
        m.illustrated_by = e.illustrated_by
        m.keywords = e.keywords
        m.quantity = e.quantity
        m.status = e.status

        return m
