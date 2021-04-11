import requests
import django.contrib.auth as auth
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from core.serializers import *
from core.models import *
from core.secrets import API_TOKEN, STRIPE_API_KEY
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


def get_category(request, category):
    category = serialize('json', Tweeprint.objects.filter(category_slug=category), fields=('id', 'date_added', 'link', 'tweet_id', 'tweet_json', 'score', 'category', 'category_slug'))
    return HttpResponse(category, content_type="application/json")

def get_categories(request):
    categories = [t[0] for t in Tweeprint.CHOICES]
    if request.method == 'GET':
        return JsonResponse(categories, safe=False)

def get_used_categories(request):
    used_categories = {t.category_slug: {'category': t.category, 'slug': t.category_slug} for t in Tweeprint.objects.all()}.values()
    if request.method == 'GET':
        return JsonResponse(list(used_categories), safe=False)

def get_tweeprints(request):
    if request.method == 'GET':
        tweeprints = serialize('json', Tweeprint.objects.all(), fields=('id', 'date_added', 'link', 'tweet_id', 'tweet_json', 'score', 'category', 'category_slug'))
        return HttpResponse(tweeprints, content_type="application/json")

def get_most_recent(request):
    if request.method == 'GET':
        tweeprints = serialize('json', Tweeprint.objects.all().order_by('-date_added'), fields=('id', 'date_added', 'link', 'tweet_id', 'tweet_json', 'score', 'category', 'category_slug'))
        return HttpResponse(tweeprints, content_type="application/json")

def get_most_popular(request):
    if request.method == 'GET':
        tweeprints = serialize('json', Tweeprint.objects.all().order_by('-score'), fields=('id', 'date_added', 'link', 'tweet_id', 'tweet_json', 'score', 'category', 'category_slug'))
        return HttpResponse(tweeprints, content_type="application/json")


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        form = request.body
        json_data = json.loads(request.body)
        try:
            tweeprint = Tweeprint.objects.create(link=str(json_data['link']), category=json_data['category'])
        except Exception as e:
            print(e)
        return HttpResponse('Submitted!')
    return HttpResponse("POST not made")