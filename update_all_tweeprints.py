from core.models import *

tweeprints = Tweeprint.objects.all()
for tweeprint in tweeprints:
    tweeprint.update_tweet_json()