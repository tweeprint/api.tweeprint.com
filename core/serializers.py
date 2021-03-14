from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.models import *

class TweeprintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tweeprint
    fields = ['date_added', 'link', 'category', 'url_ref']

  
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Tweeprint
    fields = ['category']