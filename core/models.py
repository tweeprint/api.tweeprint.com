from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.utils.text import slugify

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
    category = models.CharField(max_length=300, choices=CHOICES)
    score = models.IntegerField(default=0)
    url_ref = models.SlugField(blank=True, null=True, max_length=255)

    def __str__(self):
        return (f'{self.link} <{self.category}>')

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = timezone.now
        if not self.url_ref:
            if self.name:
                self.url_ref = slugify(self.name)
        self.tweet_id = self.link.split('/')[-1].split('?')[0]
        super(Tweeprint, self).save(*args, **kwargs)

