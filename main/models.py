from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    company = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    still_employed = models.BooleanField()
    description = models.TextField()

    objects = models.Manager()

    class Meta:
        ordering = ('-start_date'),

    def __str__(self):
        return self.title + " at " + self.company

class Skill(models.Model):
    name = models.CharField(max_length=50)

    objects = models.Manager()

    class Meta:
        ordering = ('-name'),
    
    def __str__(self):
        return self.name

class Degree(models.Model):
    kind = models.CharField(max_length=250)
    major = models.CharField(max_length=250)
    school = models.CharField(max_length=250, default='')
    icon_url = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    objects = models.Manager()

    class Meta:
        ordering = ('-start_date'),
    
    def __str__(self):
        return self.kind + " in " + self.major