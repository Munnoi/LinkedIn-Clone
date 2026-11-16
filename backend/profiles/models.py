from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="photos/", blank=True, null=True)
    cover_img = models.ImageField(upload_to="photos/", blank=True, null=True)
    headline = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True, null=True) # optional.
    website = models.URLField(blank=True, null=True) # optional.
    location = models.TextField(max_length=100, blank=True, null=True) # optional.
    phone = models.IntegerField(max_length=10, blank=True, null=True) # optional. # TODO: change the dt to 'CharField' with max_length=10.
    linkedin_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + '-' + self.company

class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200) # i reckon, this could be changed to optional.

    class Categories(models.TextChoices):
        SOFT = "SOFT", "Soft"
        TECH = "TECH", "Tech"
        PRACTICAL = "PRACTICAL", "Practical"
        EXTRA = "EXTRA", "Extra"

    category = models.CharField(max_length=9, choices=Categories.choices)

    def __str__(self):
        return f"{self.name} - {self.category}"

class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    duration = models.IntegerField()
    institution = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course} - {self.institution}"

class Certification(models.Model): # TODO: optional; will implement if it's relevant.
    pass

class TechStack(models.Model):
    tech_name = models.CharField(max_length=50)
class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tech_stack = models.ManyToManyField(TechStack)
    github = models.URLField(blank=True, null=True) # optional.
    live_link = models.URLField(blank=True, null=True) # optional.

    def __str__(self):
        return self.title
