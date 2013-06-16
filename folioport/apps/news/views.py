from django.db.models import get_model
from django.template import RequestContext
from django.shortcuts import render_to_response

News = get_model('news', 'News')


#todo change to class based views
def news(request):
    return render_to_response('pages/news.html', {'news': News.objects.all()},
        context_instance=RequestContext(request))

def news_detail(request, slug):
    return render_to_response('pages/news_details.html', {'news': News.objects.get(slug=slug)},
        context_instance=RequestContext(request))
