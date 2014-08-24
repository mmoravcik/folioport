from django.db.models import get_model
from django.conf import settings

Category = get_model('project', 'Category')
Project = get_model('project', 'Project')


def folioport_project(request):
    return {
        'folioport_project_categories' : Category.objects.filter(active=1),
        'GOOGLE_ANALYTICS_ACCOUNT': settings.GOOGLE_ANALYTICS_ACCOUNT,
        'folioport_projects': Project.active_objects.all(),
        'folioport_content_types': settings.FOLIOPORT_CONTENT_TYPES,
    }