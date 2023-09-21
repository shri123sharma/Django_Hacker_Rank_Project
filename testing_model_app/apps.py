from django.apps import AppConfig


class TestingModelAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testing_model_app'
