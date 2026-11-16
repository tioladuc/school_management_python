# Generated Django repositories

Generated from the ORM model files in the supplied `orm(1).zip` archive.

- Repositories generated: **55**.
- Excluded at your earlier instruction: `ContractModel` and `SubscriptionModel`.
- `ContractDataModel` is included because it is a distinct model in the archive; its ORM model has a foreign key to `ContractModel`.
- The ZIP contains ORM model files only. It does **not** contain mapper implementations or domain classes. Each repository therefore imports the corresponding mapper using the project naming convention and expects that mapper to implement:
  - `to_model(data, instance)`
  - `to_domain(instance)`
- Model classes are imported directly from their individual ORM modules. This avoids relying on `orm/models.py`, which in the supplied archive imports `company_model.py` even though that file is not present in the archive.

## Installation

Copy the generated files into your infrastructure repository package, alongside the existing `orm` and `mappers` packages, for example:

```text
infrastructure/
    orm/
    mappers/
    repositories/   # generated files go here
```

The repository constructor accepts a default `connection_alias`; each CRUD method also accepts an optional `db_alias` override. If omitted, the constructor's alias is used.

## Mapper naming convention

For example, `AcademicYearRepository` imports `AcademicYearMapper` from `academic_year_mapper.py`. Adjust import names if your existing mapper package uses a different convention.
