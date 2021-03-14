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

def get_categories(request):
    categories = [t[0] for t in Tweeprint.CHOICES]
    if request.method == 'GET':
        return JsonResponse(categories, safe=False)

def get_tweeprints(request):
    if request.method == 'GET':
        return JsonResponse([{"id": t.id, "category": t.category, "tweet_id": t.tweet_id} for t in Tweeprint.objects.all()],safe=False)

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