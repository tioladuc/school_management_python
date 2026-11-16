
import importlib
import inspect
import pkgutil
import re

from apps.company_context.application import dto
from apps.company_context.infrastructure import repositories


class SchoolApplicationService:

    def __init__(self, events=None):
        self.events = events
        self.repositories = self._register_repositories()

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

    def _register_repositories(self):

        # Discover all DTO classes
        dto_classes = self._discover_classes(
            dto,
            "Dto"
        )

        # Discover all repository classes
        repository_classes = self._discover_classes(
            repositories,
            "Repository"
        )

        registered = {}
        missing = []

        # Associate each DTO with its repository
        for key, dto_class in dto_classes.items():

            repository_class = repository_classes.get(key)

            if repository_class is None:
                missing.append(dto_class.__name__)
                continue

            registered[dto_class] = repository_class()

        if missing:
            raise ImportError(
                "Missing repositories for DTOs: "
                + ", ".join(sorted(missing))
            )

        return registered

    def _get_repository(self, dto):

        repository = self.repositories.get(dto)

        if repository is None:
            raise ValueError(
                f"No repository registered for {dto.__name__}"
            )

        return repository

    def get_all(self, dto, db_alias="default"):

        repository = self._get_repository(dto)

        entities = repository.get_all(db_alias)

        return [
            dto.to_dto(entity)
            for entity in entities
        ]

    def get_by_id(self, dto, id, db_alias="default"):

        repository = self._get_repository(dto)

        entity = repository.get_by_id(id, db_alias)

        if entity is None:
            return None

        return dto.to_dto(entity)

    def save(self, dto, data, db_alias="default"):

        repository = self._get_repository(dto)

        # DTO -> Domain Entity
        entity = dto.to_domain(data)

        # Domain Entity -> Persisted Domain Entity
        saved_entity = repository.save(
            None,
            entity,
            db_alias
        )

        # Persisted Domain Entity -> DTO
        return dto.to_dto(saved_entity)

    def delete(self, dto, id, db_alias="default"):

        repository = self._get_repository(dto)

        return repository.delete(id, db_alias)
