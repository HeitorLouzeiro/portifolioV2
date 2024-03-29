from django.db import models


# Create your models here.
class PersonalData(models.Model):
    name = models.CharField(max_length=30)
    title = models.TextField()
    cover = models.ImageField(
        upload_to='portifolio/user/cover/', blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=50)
    aboutme = models.TextField()

    def __str__(self):
        return self.title


class Card(models.Model):
    SECTION = (
        ('1', 'Services'),
        ('2', 'Expirience'),
        ('3', 'Curriculum'),
        ('4', 'Portfolio'),
    )
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=20, null=True, blank=True)
    linkgithub = models.CharField(max_length=100, null=True, blank=True)
    linkdeploy = models.CharField(max_length=100, null=True, blank=True)
    datainfo = models.CharField(max_length=30, null=True, blank=True)
    section = models.CharField(max_length=1, choices=SECTION)
    cover = models.ImageField(
        upload_to='portifolio/projects/cover/', blank=True)

    def __str__(self):
        return self.title+" "+self.section

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)
