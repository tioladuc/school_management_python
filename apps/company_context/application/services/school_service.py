
import importlib
import inspect
import pkgutil
import re

from apps.company_context.application import dto
from apps.company_context.infrastructure import repositories


class SchoolApplicationService:

    def __init__(self, events=None):
        self.events = events
        self.repositories = {}

    @staticmethod
    def _normalize_name(name):
        """Normalize class names for matching."""
        return re.sub(r"[^a-z0-9]", "", name.lower())

    @staticmethod
    def _discover_classes(package, suffix):
        discovered = {}

        for module_info in pkgutil.iter_modules(package.__path__):

            module_name = (
                f"{package.__name__}.{module_info.name}"
            )

            module = importlib.import_module(module_name)

            for _, cls in inspect.getmembers(
                module,
                inspect.isclass
            ):

                # Ignore imported classes
                if cls.__module__ != module.__name__:
                    continue

                if cls.__name__.endswith(suffix):

                    key = SchoolApplicationService._normalize_name(
                        cls.__name__[:-len(suffix)]
                    )

                    discovered[key] = cls

        return discovered

    def _register_repositories(self, db_alias="default"):

        dto_classes = self._discover_classes(dto, "Dto")

        repository_classes = self._discover_classes(
            repositories,
            "Repository"
        )

        registered = {}
        missing = []

        for key, dto_class in dto_classes.items():

            repository_class = repository_classes.get(key)

            if repository_class is None:
                missing.append(dto_class.__name__)
                continue

            registered[dto_class] = repository_class(db_alias)

        if missing:
            raise ImportError(
                "Missing repositories for DTOs: "
                + ", ".join(sorted(missing))
            )

        return registered

    def _get_repository(self, dto, db_alias="default"):

        if dto not in self.repositories:
            self.repositories[dto] = self._register_single_repository(
                dto,
                db_alias
            )

        return self.repositories[dto]

    def _register_single_repository(self, dto, db_alias):

        key = self._normalize_name(
            dto.__name__[:-3]
        )

        repository_classes = self._discover_classes(
            repositories,
            "Repository"
        )

        repository_class = repository_classes.get(key)

        if repository_class is None:
            raise ValueError(
                f"No repository found for {dto.__name__}"
            )

        return repository_class(db_alias)

    def get_all(self, dto, db_alias="default"):

        repository = self._get_repository(dto, db_alias)

        #entities = repository.get_all(db_alias)

        return [
            dto.to_dto(entity)
            for entity in repository.get_all(db_alias)
        ]

    def get_search(self, dto, search: dict, db_alias="default"):
    
        repository = self._get_repository(dto, db_alias)
    
        #entities = repository.get_all(db_alias)
    
        return [
            dto.to_dto(entity)
            for entity in repository.get_search(search, db_alias)
        ]
    

    def get_by_id(self, dto, id, db_alias="default"):

        repository = self._get_repository(dto, db_alias)

        entity = repository.get_by_id(id, db_alias)

        if entity is None:
            return None

        return dto.to_dto(entity)

    def save(self, dto, data, db_alias="default"):
        print('MMMMMMMMM save 01')
        repository = self._get_repository(dto, db_alias)
        print('MMMMMMMMM save 02')
        # DTO -> Domain Entity
        entity = dto.to_domain(data)
        print('MMMMMMMMM save 03')
        # Domain Entity -> Persisted Domain Entity
        saved_entity = repository.save(
            data.id if hasattr(data, 'id') else None,
            entity,
            db_alias
        )
        print('MMMMMMMMM save 04')

        # Persisted Domain Entity -> DTO
        return dto.to_dto(saved_entity)

    def delete(self, dto, id, db_alias="default"):

        repository = self._get_repository(dto, db_alias)

        return repository.delete(id, db_alias)
