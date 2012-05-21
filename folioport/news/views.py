from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from folioport.news.models import News


def news(request):
    return render_to_response('pages/news.html', {'news': News.objects.all()}, context_instance=RequestContext(request))

def news_detail(requestm, slug):
    return render_to_response('pages/news_details.html', {'news': News.objects.get(slug=slug)}, context_instance=RequestContext(request))
