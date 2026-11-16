# Generated domain entities

Generated from `orm(1).zip` by inspecting the Django model field declarations.

- One dataclass per included ORM model.
- Foreign keys are represented as scalar `<field>_id` attributes.
- Django's implicit primary key is represented as `id: int | None = None`.
- `auto_now` and `auto_now_add` timestamps are optional in the domain entity.
- Model defaults and blank text defaults are reflected where statically declared.
- `ContractModel` and `SubscriptionModel` are excluded, as requested.
- `ContractDataModel` is retained because it was not explicitly excluded; its `contract_id` refers to the excluded Contract model and therefore requires that relationship to be handled outside this generated entity package if the model itself is also removed.

## Integration

Place these files under `domain/entities/`. Imports follow the convention:

```python
from ...domain.entities.school import School
```

These entities are dataclasses and do not import Django. Review business invariants and validation rules before using them as production domain objects.
