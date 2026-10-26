class TenantDatabaseRouter:
    def db_for_read(self, model, **hints):
        from django.db import connections

        # Use the alias set by middleware for this request.
        # See the request-context implementation below.
        from config.tenant_context import get_current_db_alias

        alias = get_current_db_alias()

        if alias and alias in connections.databases:
            return alias

        return "default"

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return obj1._state.db == obj2._state.db

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Adapt this policy if tenant databases need their own migrations.
        return db == "default"