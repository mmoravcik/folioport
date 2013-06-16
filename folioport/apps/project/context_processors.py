from django.db.models import get_model

Category = get_model('project', 'Category')


def folioport_project(request):
    return {
        'folioport_project_categories' : Category.objects.filter(active=1),
    }