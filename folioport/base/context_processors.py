from django.db.models import get_model
from django.conf import settings

Category = get_model('project', 'Category')
Project = get_model('project', 'Project')
Page = get_model('page', 'Page')


def folioport_project(request):
    return {
        'folioport_project_categories' : Category.objects.active(),
        'folioport_project_categories_with_projects' : Category.objects.active().exclude(project=None),
        'GOOGLE_ANALYTICS_ACCOUNT': settings.GOOGLE_ANALYTICS_ACCOUNT,
        'folioport_projects': Project.objects.active(),
        'folioport_projects_without_category': Project.objects.active().filter(category=None),
        'folioport_content_types': settings.FOLIOPORT_CONTENT_TYPES,
        'folioport_pages': Page.objects.active().exclude(type=Page.LANDING_PAGE),
        'folioport_date_format': 'j N Y',
    }