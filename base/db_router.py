class HistoryRouter:
    def db_for_read(self, model, **hints):
        if hasattr(model, '_meta') and 'historical' in model._meta.model_name.lower():
            return 'history_db'
        return None

    def db_for_write(self, model, **hints):
        if hasattr(model, '_meta') and 'historical' in model._meta.model_name.lower():
            return 'history_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name and 'historical' in model_name.lower():
            return db == 'history_db'
        elif db == 'history_db':
            return model_name and 'historical' in model_name.lower()
        return None