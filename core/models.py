from django.db import models


# Create your models here.
class PersonalData(models.Model):
    name = models.CharField(max_length=30)
    title = models.TextField()
    cover = models.ImageField(
        upload_to='portifolio/user/cover/', blank=True)

    def __str__(self):
        return self.name
