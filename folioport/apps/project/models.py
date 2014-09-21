from folioport.apps.project.abstract_models import AbstractProject
from folioport.base.abstract_models import AbstractCategory


class Category(AbstractCategory):
    @staticmethod
    def get_form_class():
        from folioport.apps.project.forms import CategoryForm
        return CategoryForm


class Project(AbstractProject):
    pass