from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=250, default='')
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    about = models.TextField()
    linkedin_url = models.CharField(max_length=250, default='')
    github_url = models.CharField(max_length=250, default='')
    created = models.DateTimeField(auto_now_add=True)
    color_main = models.CharField(max_length=6, default='007BFF')
    color_accent = models.CharField(max_length=6, default='4682B4')
    color_text = models.CharField(max_length=6, default='000000')
    color_background = models.CharField(max_length=6, default='FFFFFF')
    title_section_1 = models.CharField(max_length=50, default='About')
    title_section_2 = models.CharField(max_length=50, default='Experience')
    title_section_3 = models.CharField(max_length=50, default='Education')
    title_section_4 = models.CharField(max_length=50, default='Skills')
    title_section_5 = models.CharField(max_length=50, default='Portfolio')
    skill_category_1 = models.CharField(max_length=50, default='Languages')
    skill_category_2 = models.CharField(max_length=50, default='Frameworks')
    skill_category_3 = models.CharField(max_length=50, default='Tools')

    objects = models.Manager()

    class Meta:
        ordering = ('-created'),

    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=250, default='')
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
    CATEGORY_CHOICES = (
        ('category-1', 'Category-1'),
        ('category-2', 'Category-2'),
        ('category-3', 'Category-3'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='category-1')

    objects = models.Manager()

    class Meta:
        ordering = ('-name'),
    
    def __str__(self):
        return self.name

class Degree(models.Model):
    kind = models.CharField(max_length=250)
    major = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    icon_url = models.CharField(max_length=250, default='')
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    objects = models.Manager()

    class Meta:
        ordering = ('-start_date'),
    
    def __str__(self):
        return self.kind + " in " + self.major

class Project(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=250, default='')
    subheading = models.CharField(max_length=250)
    description = models.TextField()
    link_url = models.CharField(max_length=250, default='')

    objects = models.Manager()

    class Meta:
        ordering = ('-name'),
    
    def __str__(self):
        return self.name