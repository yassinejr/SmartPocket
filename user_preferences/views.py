from django.shortcuts import render
from django.conf import settings
from .models import *
import os
import json


# Create your views here.
def index(request):
    user_preferences_exists = UserPreferences.objects.filter(user=request.user).exists()
    user_preferences = None

    currency_data = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    with open(file_path) as json_file:
        data = json.load(json_file)
        for i, j in data.items():
            currency_data.append({'code': i, 'name': j})

    if user_preferences_exists:
        user_preferences = UserPreferences.objects.get(user=request.user)

    if request.method == 'GET':

        context = {'currency_data': currency_data, 'user_preferences': user_preferences}
        return render(request, 'user_preferences/preferences.html', context)

    elif request.method == 'POST':
        currency = request.POST['currency']
        if user_preferences_exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreferences.objects.create(user=request.user, currency=currency)

        context = {'currency': currency, 'user_preferences': user_preferences}
        return render(request, 'user_preferences/preferences.html', context)
    else:
        pass