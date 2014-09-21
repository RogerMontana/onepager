
from django.http.response import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from models import Main, News
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.core.context_processors import csrf
#/Users/artem/Documents/Projects/trex_webpage/bin/trex_app/assets
#/Users/artem/Downloads/foundation5/foundation-5.2.3
# Create your views here.


def index(request):
    data={}
    template = 'index.html'
    try:
        data['all_news'] = News.objects.all()
        data['contacts'] = Main.objects.get(id = 1)
        data['hello'] = Main.objects.get(id = 1)
        data['button_url'] = Main.objects.get(id = 1)
        data['news_text'] = Main.objects.get(id = 1)
        data['button_url2'] = Main.objects.get(id = 1)
        data['news_text2'] = Main.objects.get(id = 1)
        data['button_url3'] = Main.objects.get(id = 1)
        data['news_text3'] = Main.objects.get(id = 1)
        data['button_url4'] = Main.objects.get(id = 1)
        data['news_text4'] = Main.objects.get(id = 1)
        data['about_us'] = Main.objects.get(id = 1)
    except:
        print("empty database")
        #raise Http404
        pass
    return render_to_response(template,data)
