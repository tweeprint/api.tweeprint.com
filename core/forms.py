from django import forms
from django.contrib.auth import authenticate, login
from django.core.validators import MinLengthValidator
from .models import *
