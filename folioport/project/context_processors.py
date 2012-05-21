from folioport.project.models import Category

def folioport_project(request):
    return {
        'project_categories' : Category.objects.filter(active=1),
    }