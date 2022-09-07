from django.apps import AppConfig


# Inherited Appconfig and made PagesConfig 
class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
