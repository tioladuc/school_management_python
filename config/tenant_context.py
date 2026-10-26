from contextvars import ContextVar

_current_db_alias = ContextVar("current_db_alias", default=None)


def get_current_db_alias():
    return _current_db_alias.get()


def set_current_db_alias(alias):
    return _current_db_alias.set(alias)


def reset_current_db_alias(token):
    _current_db_alias.reset(token)