"""Repository for FeeOnlineCoursePaymentModel."""

from ..orm.fee_online_course_payment_model import FeeOnlineCoursePaymentModel
from ..mappers.fee_online_course_payment_mapper import FeeOnlineCoursePaymentMapper


class FeeOnlineCoursePaymentRepository:
    """Persistence operations for FeeOnlineCoursePaymentModel.

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
        return FeeOnlineCoursePaymentModel.objects.using(self._db_alias(db_alias)).all()

    def get_by_id(self, object_id, db_alias=None):
        """Return one record by primary key, or None when it does not exist."""
        return (
            FeeOnlineCoursePaymentModel.objects.using(self._db_alias(db_alias))
            .filter(pk=object_id)
            .first()
        )

    def save(self, object_id, data, db_alias=None):
        """Create or update a record and return its domain representation."""
        alias = self._db_alias(db_alias)

        if object_id is not None:
            obj = (
                FeeOnlineCoursePaymentModel.objects.using(alias)
                .filter(pk=object_id)
                .first()
            )
            if obj is None:
                raise ValueError(
                    f"{FeeOnlineCoursePaymentModel.__name__} {object_id} does not exist."
                )
        else:
            obj = FeeOnlineCoursePaymentModel()

        FeeOnlineCoursePaymentMapper.to_model(data, obj)
        obj.save(using=alias)
        return FeeOnlineCoursePaymentMapper.to_domain(obj)

    def delete(self, object_id, db_alias=None):
        """Delete a record by primary key; return Django's delete result."""
        return (
            FeeOnlineCoursePaymentModel.objects.using(self._db_alias(db_alias))
            .filter(pk=object_id)
            .delete()
        )
