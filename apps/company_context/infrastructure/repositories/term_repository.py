"""Repository for TermModel."""

from ..orm.term_model import TermModel
from ..mappers.term_mapper import TermMapper


class TermRepository:
    """Persistence operations for TermModel.

    ``connection_alias`` is the default Django database alias used by this
    repository. A method-level ``db_alias`` can override it when necessary.
    The mapper is expected to expose ``to_model(data, instance)`` and
    ``to_domain(instance)`` as in the project's repository convention.
    """

    def __init__(self, connection_alias="default"):
        self.connection_alias = connection_alias or "default"

    def _db_alias(self, db_alias=None):
        return db_alias or self.connection_alias

    def get_all(self, db_alias=None):
        """Return all records as a Django QuerySet."""
        return TermModel.objects.using(self._db_alias(db_alias)).all()

    def get_by_id(self, object_id, db_alias=None):
        """Return one record by primary key, or None when it does not exist."""
        return (
            TermModel.objects.using(self._db_alias(db_alias))
            .filter(pk=object_id)
            .first()
        )

    def save(self, object_id, data, db_alias=None):
        """Create or update a record and return its domain representation."""
        alias = self._db_alias(db_alias)

        if object_id is not None:
            obj = (
                TermModel.objects.using(alias)
                .filter(pk=object_id)
                .first()
            )
            if obj is None:
                raise ValueError(
                    f"{TermModel.__name__} {object_id} does not exist."
                )
        else:
            obj = TermModel()

        TermMapper.to_model(data, obj)
        obj.save(using=alias)
        return TermMapper.to_domain(obj)

    def delete(self, object_id, db_alias=None):
        """Delete a record by primary key; return Django's delete result."""
        return (
            TermModel.objects.using(self._db_alias(db_alias))
            .filter(pk=object_id)
            .delete()
        )
