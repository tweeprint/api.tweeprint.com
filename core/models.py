from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.utils.text import slugify
import tweepy
from tweepy.auth import AppAuthHandler
from .secrets import TWITTER_API_KEY, TWITTER_API_SECRET

class Tweeprint(models.Model):

    class Meta:
        db_table = "tweeprints"
        ordering = ["-date_added"]
    
    CHOICES = [
        ('Animal Behavior and Cognition', 'Animal Behavior and Cognition'),
        ('Behavioural Neuroscience', 'Behavioural Neuroscience'),
        ('Biochemistry', 'Biochemistry'),
        ('Bioengineering', 'Bioengineering'),
        ('Bioinformatics', 'Bioinformatics'),
        ('Biophysics', 'Biophysics'),
        ('Cancer Biology', 'Cancer Biology'),
        ('Cell Biology', 'Cell Biology'),
        ('Cognitive Science', 'Cognitive Science'),
        ('Developmental Biology', 'Developmental Biology'),
        ('Ecology', 'Ecology'),
        ('Evolutionary Biology', 'Evolutionary Biology'),
        ('Genetics', 'Genetics'),
        ('Genomics', 'Genomics'),
        ('Immunology', 'Immunology'),
        ('Microbiology', 'Microbiology'),
        ('Molecular Biology', 'Molecular Biology'),
        ('Molecular Neuroscience', 'Molecular Neuroscience'),
        ('Motor Neuroscience', 'Motor Neuroscience'),
        ('Neuroscience', 'Neuroscience'),
        ('Paleontology', 'Paleontology'),
        ('Pathology', 'Pathology'),
        ('Pharmacology and Toxicology', 'Pharmacology and Toxicology'),
        ('Physiology', 'Physiology'),
        ('Plant Biology', 'Plant Biology'),
        ('Psychology', 'Psychology'),
        ('Psychophysics', 'Psychophysics'),
        ('Scientific Communication and Education', 'Scientific Communication and Education'),
        ('Synthetic Biology', 'Synthetic Biology'),
        ('Structural Biology', 'Structural Biology'),
        ('Systems Biology', 'Systems Biology'),
        ('Systems Neuroscience', 'Systems Neuroscience'),
        ('Zoology', 'Zoology'),

    ]

    name = models.CharField(max_length=300, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    link = models.URLField(unique=True)
    tweet_id = models.CharField(max_length=300, blank=True, null=True)
    tweet_text = models.CharField(max_length=1000, blank=True, null=True)
    tweet_json = models.JSONField(null=True)
    category = models.CharField(max_length=300, choices=CHOICES)
    category_slug = models.SlugField(max_length=300, default="", blank=True, null=True)
    score = models.IntegerField(default=0)
    url_ref = models.SlugField(blank=True, null=True, max_length=255)

    def __str__(self):
        return (f'{self.link} <{self.category}>')

    def get_tweet(self):
        auth = AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        api = tweepy.API(auth)
        tweet = api.get_status(self.tweet_id, tweet_mode="extended")
        try:
            self.tweet_text = tweet.retweeted_status.full_text
        except AttributeError:
            self.tweet_text = tweet.full_text
            self.tweet_json = tweet._json
        return tweet
    

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = timezone.now
        if not self.url_ref:
            if self.name:
                self.url_ref = slugify(self.name)
        self.tweet_id = self.link.split('/')[-1].split('?')[0]
        self.category_slug = slugify(self.category)
        self.get_tweet()
        super(Tweeprint, self).save(*args, **kwargs)
